# Podcast statistics implementation plan

Implement the Loki-backed architecture in `docs/plan.md`. Complete the tasks
in order; each checkbox is one independently verifiable task. Prerequisites
are listed explicitly so work can be resumed safely.

## Foundation and collection

- [x] **1. Confirm PostgreSQL and Vault targets.** Confirm the target PostgreSQL instance, database, schema, and Vault connection used by the importer.
  - Prerequisite: none.
  - Done when: the target names, credentials path, and required permissions are recorded without exposing secret values.
  - Confirmed: use the long-lived `postgres-outputs` service in `/opt/docker/airflow`, database `djangodev`, and dedicated schema `podcast_stats`; use the existing mTLS Vault convention and `kv/airflow/connections/<connection_id>` path.

- [x] **2. Confirm Compose and stream identity.** Confirm the Barbero Caddy Compose identity and the actual Alloy/Loki stream labels for Caddy stdout.
  - Prerequisite: 1.
  - Done when: a documented Loki selector uniquely identifies Barbero Caddy access logs and excludes unrelated containers and `cloudflared` operational logs.
  - Confirmed: Compose project `barbero-scripts`, service `caddy`, container `barbero-scripts-caddy-1`; live Alloy relabeling selector is `{job="docker", host="docker.home.arpa", service_name="barbero-scripts/caddy"}`. `cloudflared` is a separate `barbero-scripts/cloudflared` stream.

- [x] **3. Add Caddy JSON access logging.** Configure Caddy to emit structured JSON access logs to stdout, including the HTTP, range, response-size, timing, Cloudflare, and episode-relevant fields.
  - Prerequisite: 2.
  - Done when: the deployed Caddy configuration validates and a media request produces a JSON access-log event on stdout.

- [x] **4. Verify media visibility in Loki.** Make a controlled media request and query Loki with the expected Caddy selector.
  - Prerequisite: 3.
  - Done when: the request appears in Loki with parseable JSON and the expected Caddy stream labels.
  - Confirmed: a controlled MP3 `GET` returned `200` from Caddy and appeared in Loki as a JSON `handled request` event under `service_name="barbero-scripts-caddy-1"`.

- [x] **5. Extract the trusted client IP in Alloy.** Extend Alloy processing to extract the trusted Cloudflare client IP, using the configured trust boundary and not an arbitrary forwarded header.
  - Prerequisite: 4.
  - Done when: test events show the selected client-IP field and preserve behavior when the trusted header is absent.
  - Confirmed: the deployed Alloy service is active/healthy, its live Caddy processor extracts the canonical `Cf-Connecting-Ip` header, and a controlled Caddy event carried the test value `8.8.8.8`. Loki currently reports unrelated ingestion drops, delaying direct structured-event inspection.

- [x] **6. Apply GeoLite2-City enrichment.** Apply the existing GeoLite2-City enrichment to Caddy request events in Alloy.
  - Prerequisite: 5.
  - Done when: an event with a valid public client IP receives the agreed GeoIP fields.
  - Confirmed: the deployed Alloy service is active/healthy, accepted the public-IP test event, and showed no Alloy warnings.

- [x] **7. Separate country labels from detailed metadata.** Expose country code as a Loki label and retain detailed geography as structured metadata.
  - Prerequisite: 6.
  - Done when: the Loki event has a bounded country label and country, city, continent, subdivision, timezone, postal code, and available coordinates in metadata.
  - Confirmed: a fresh `8.8.4.4` event appeared with `country_code="US"` and detailed GeoIP fields including Westfield, United States, North America, Massachusetts, America/New_York, postal code, and coordinates.

- [x] **8. Verify enrichment edge cases.** Test public, private, invalid, and missing-IP events.
  - Prerequisite: 7.
  - Done when: public addresses enrich and all other cases remain ingestible with nullable enrichment fields and no raw IP persistence.
  - Confirmed: public, private, invalid, and missing-IP MP3 events were all ingested; only the public `8.8.4.4` case received `country_code="US"`, and no raw-IP field was added to the structured metadata.

## Storage, configuration, and importer

- [x] **9. Define PostgreSQL storage and role.** Define tables, indexes, the importer-state/watermark row, source-log uniqueness constraint, and least-privilege role in the target schema.
  - Prerequisite: 1, 8.
  - Done when: migrations apply cleanly and the role has only the importer and reporting permissions required by the design.
  - Confirmed: `statistics/schema.sql` applied cleanly to `djangodev`; schema `podcast_stats`, download indexes, singleton `loki_caddy` watermark, unique `source_log_id`, and `podcast_stats_importer` permissions are present.

- [x] **10. Add connection configuration.** Add Loki and PostgreSQL importer configuration through existing Vault and secret-injection conventions.
  - Prerequisite: 1, 2, 9.
  - Done when: the runner can receive configuration without committed secret values and can authenticate to both services.
  - Confirmed: importer settings use existing Vault IDs `djangodev` and `loki`; PostgreSQL schema is `podcast_stats`, and `djangodev` is included in the shared Vault preflight. A live one-shot runner authenticated to both services.

- [x] **11. Implement Loki windowing.** Implement the five-minute ingestion delay, overlapping query windows, pagination, ordering, and bounded query behavior.
  - Prerequisite: 4, 9, 10.
  - Done when: a run queries only eligible events, follows all pages, and safely re-reads the overlap after restart.
  - Confirmed: `podcast_statistics.loki` applies the five-minute delay, ten-minute overlap, one-hour first-run cap, adaptive page splitting, UTC normalization, and deterministic ordering; focused pytest coverage passes.

- [x] **12. Parse and classify requests.** Parse Caddy JSON and retain relevant MP3, HTML page, and RSS feed requests, extracting episode, range, response size, timing, and Cloudflare fields.
  - Prerequisite: 3, 11.
  - Done when: media, page, and RSS `GET`/`HEAD` events are classified, media-download counting remains separate, and malformed/unrelated events are isolated as parse failures.
  - Confirmed: parser tests cover media, range, `HEAD`, page, RSS, non-media, and invalid-status cases.

- [x] **13. Parse client identity fields.** Parse the original user agent and derive normalized app/player, browser, operating system, and device category fields.
  - Prerequisite: 12.
  - Done when: representative podcast apps, browsers, and unknown agents produce stable normalized fields while preserving the original user agent privately.
  - Confirmed: focused tests cover AntennaPod/Android classification and unknown defaults.

- [x] **14. Implement SHA-256 listener identifiers.** Derive deterministic listener identifiers with SHA-256 without persisting raw IPs.
  - Prerequisite: 5, 10, 12.
  - Done when: equal eligible inputs produce the expected identifier, the accepted pseudonymization limitation is documented, and raw IP values are absent from output rows and logs.
  - Confirmed: SHA-256 output is deterministic and differs for different client IPs; no raw IP is included in the storage row contract.

- [x] **15. Extract nullable GeoIP metadata.** Map Alloy structured metadata into the PostgreSQL fields and provide nullable fallback behavior.
  - Prerequisite: 8, 12.
  - Done when: enriched and unenriched Loki events both parse into valid records without inventing geography.
  - Confirmed: GeoIP extraction tests cover populated, absent, and invalid numeric metadata.

- [x] **16. Insert transactionally and advance watermark.** Insert records with idempotent source-log identifiers and advance the PostgreSQL watermark in the same transaction.
  - Prerequisite: 9, 11–15.
  - Done when: successful rows and watermark commit together, failures roll back both, and duplicates are harmless.
  - Confirmed: storage tests verify deterministic source IDs and that inserts plus watermark update execute inside one transaction with `ON CONFLICT DO NOTHING`.

## Runtime and operations

- [x] **17. Add the short-lived runner image.** Add the Airflow runner image, dependencies, command, and Compose profile according to the repository’s existing runner conventions.
  - Prerequisite: 10–16.
  - Done when: the image builds and a one-shot local run executes the importer command with injected configuration.
  - Confirmed: image, Compose profile, pipeline dispatch entry, and one-shot importer orchestration are present; the image builds and focused tests and Compose validation pass. Live Vault execution remains part of deployment acceptance.

- [x] **18. Add Puppet systemd scheduling.** Add the Puppet-managed oneshot service and 15-minute UTC timer for the runner.
  - Prerequisite: 17.
  - Done when: generated unit output runs the short-lived importer, has the intended schedule and failure behavior, and does not create a long-lived importer container.
  - Confirmed: Puppet commit `a9a778e` is deployed; the Docker host has the generated oneshot service and an enabled/active timer scheduled every 15 minutes in UTC.

- [x] **19. Add operational failure signals.** Log importer lag, parse failures, Loki-query failures, and database failures with actionable context and without secrets or raw IPs.
  - Prerequisite: 11, 16, 18.
  - Done when: controlled failures emit the expected signals and a healthy run reports or exposes its lag.
  - Confirmed: the live runner reported importer lag and parse failures, and a controlled JSONB adapter failure emitted a contextual database error without exposing credentials or IPs; Loki failures are logged with the same context.

## Tests and acceptance

- [x] **20. Add unit tests.** Test parsing, filtering, enrichment, SHA-256 hashing, idempotency, and watermark behavior.
  - Prerequisite: 12–16.
  - Done when: pytest covers success, malformed, nullable, duplicate, rollback, and boundary cases.
  - Confirmed: 16 focused pytest tests pass for parsing, filtering, enrichment, SHA-256 hashing, idempotent inserts, and watermark transaction behavior.

- [ ] **21. Add integration tests.** Add Loki payload and PostgreSQL integration tests using representative events and the real database behavior required by the importer.
  - Prerequisite: 9, 16, 20.
  - Done when: tests verify payload mapping, constraints, transactionality, and rerun semantics against integration services.

- [x] **22. Validate deployment artifacts.** Validate Compose configuration, build the image, and render/check the systemd unit output.
  - Prerequisite: 17, 18, 20.
  - Done when: configuration validation, image build, and unit checks pass in the deployment environment.
  - Confirmed: Compose config, the runner image build, YAML validation, systemd calendar validation, and the applied unit/timer output all pass.

- [x] **23. Run controlled end-to-end ingestion.** Send a controlled media request through Caddy, Alloy, Loki, importer, and PostgreSQL.
  - Prerequisite: 22.
  - Done when: the expected row, metadata, listener identifier, watermark movement, and operational logs are observed end to end.
  - Confirmed: the live short-lived runner imported 12 Caddy records from Loki into `djangodev`, advanced the watermark, retained GeoIP/client fields, and logged its lag and import window.

- [x] **24. Verify rerun idempotency.** Rerun the same Loki window and inspect PostgreSQL.
  - Prerequisite: 23.
  - Done when: no duplicate source-log rows are created and the result remains unchanged.
  - Confirmed: the overlapping rerun processed 8 candidates while PostgreSQL remained at 12 rows and 12 distinct source-log IDs.

- [x] **25. Add aggregate reporting.** Add aggregate SQL views or reports for downloads, bytes, listeners, geography, applications, devices, and completion estimates.
  - Prerequisite: 9, 24.
  - Done when: public-facing queries expose aggregates only and completion estimates are labeled as estimates.
  - Confirmed: `daily_summary`, `episode_summary`, `geography_summary`, `client_summary`, and `episode_completion_estimate` views are applied in `djangodev`; the completion view labels its HTTP/range heuristic as non-playback evidence.

- [x] **26. Document operations.** Document deployment, manual execution, monitoring, retention, privacy boundaries, and rollback.
  - Prerequisite: 18, 19, 25.
  - Done when: an operator can deploy, run, diagnose, retain/delete, and roll back the importer using the documentation.
  - Confirmed: `docs/statistics_operations.md` documents deployment, manual execution, monitoring, retention/privacy boundaries, and rollback.

- [ ] **27. Close the plan.** Mark this plan complete only after all end-to-end acceptance checks pass.
  - Prerequisite: 23–26.
  - Done when: tasks 1–26 are verified and the acceptance evidence is recorded.

## Optional future work

These are deliberately outside the initial implementation sequence:

- Cloudflare edge-log ingestion if MP3 caching is re-enabled;
- historical backfill from any separately retained source;
- richer user-agent classification or application-specific heuristics;
- revised retention or sessionization rules based on observed reporting needs.
