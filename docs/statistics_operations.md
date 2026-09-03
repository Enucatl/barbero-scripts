# Podcast statistics operations

## Deployment

Deploy the Airflow `main` branch, then deploy the Puppet `production` branch
and apply Puppet on the Docker host. The latter installs and enables
`automation-podcast-statistics.timer`; the service itself is a short-lived
oneshot. The runner uses the existing Vault connections `loki` and `djangodev`
and the `podcast_stats` schema in the `postgres-outputs` database.

## Manual execution and monitoring

Run the same command as the timer from `/opt/docker/airflow`:

```text
docker compose --profile runner run --build --rm --no-deps podcast-statistics
```

Inspect the timer with `systemctl list-timers automation-podcast-statistics.timer`
and service output with `journalctl -u automation-podcast-statistics.service`.
The runner logs its Loki window, importer lag, parse failures, query failures,
database failures, and successful row count. A failed transaction leaves the
watermark unchanged and is retried by the next overlapping run.

## Storage, privacy, and retention

PostgreSQL is the durable store and Loki is only the ingestion buffer. Public
dashboards must use the aggregate views in `podcast_stats`; do not expose raw
rows, original user agents, detailed geography, listener hashes, or request
paths publicly. Raw IP addresses are never stored. Apply retention and deletion
to both PostgreSQL raw rows and the corresponding Loki stream according to the
operator's approved privacy policy; the aggregate views contain no separate
copy of raw events.

## Rollback

Disable the timer before rollback if repeated failures are urgent:

```text
systemctl disable --now automation-podcast-statistics.timer
```

Revert the Airflow deployment and Puppet revision independently, then restore
the prior runner image or schema migration as appropriate. Do not delete the
watermark or raw rows during a code rollback; the source-log uniqueness key
makes a later replay safe.
