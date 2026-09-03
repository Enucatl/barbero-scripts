# Podcast statistics architecture

This is the authoritative product and architecture decision for Barbero
statistics. It supersedes the earlier host-mounted Caddy log file proposal.

## Architecture

```text
Caddy JSON stdout
  → host Alloy Docker scrape
  → Loki
  → scheduled Airflow runner
  → existing postgres-outputs PostgreSQL
```

Caddy is the source of request logs. `cloudflared` operational logs are not
used for podcast statistics. Alloy and Loki are the existing collection path;
the statistics importer queries Loki rather than reading a host log file.

The importer is a short-lived Airflow runner invoked by a Puppet-managed
systemd oneshot service and 15-minute UTC timer. PostgreSQL is the durable
store. Loki is an ingestion buffer, not the system of record.

## Metric and ingestion semantics

The listening metric is downloaded MP3 data. A successful media `GET` is
evidence that an application requested audio, not proof that a person played
or heard it. Initially, Cloudflare caching for MP3 paths is disabled so media
requests reach Caddy and enter the collection path. Requests served from a
Cloudflare cache are explicitly outside the initial metric.

The collector also retains relevant HTML page and RSS feed requests. These
support visitor and subscriber-interest reporting, but are separate from the
MP3 download/listening metric.

The importer waits for a five-minute ingestion delay, then processes
overlapping Loki query windows. A PostgreSQL watermark records progress, while
an idempotent source-log identifier makes overlap and retries safe. The
watermark advances only with the corresponding transactional inserts.

Loki query and parsing failures must not affect Caddy or audio delivery.

## Data and privacy boundary

Raw IP addresses are never stored in PostgreSQL or exposed in public reports.
The trusted Cloudflare client IP is pre-hashed in the existing GeoLite2-City
Alloy pipeline. Enrichment is null-tolerant: missing, invalid, private, or
unresolved addresses do not prevent a request from being ingested.

Retain these GeoIP fields when available:

- country code and country name;
- city;
- continent;
- subdivision;
- timezone;
- postal code;
- latitude and longitude.

Retain these client fields:

- original user agent;
- normalized application/player;
- browser;
- operating system;
- device category.

Retain the HTTP and media facts needed for reporting: timestamp, method,
status, request path, response size, requested byte range, request timing,
Cloudflare request metadata, and normalized episode fields. Listener
identifiers are SHA-256-derived and must not include the raw IP in the stored
field.

Public reporting is aggregate-only. Raw request data, original user agents,
listener identifiers, detailed geography, and other identifying or
quasi-identifying fields remain inside the controlled retention boundary.
Retention and deletion rules must be documented with deployment operations.

## Reporting scope and non-goals

Reports may aggregate downloads, bytes, approximate listeners, geography,
applications, devices, and completion estimates. Completion remains an
estimate based on HTTP response and range evidence.

This system does not aim to:

- prove playback or listening completion;
- identify people;
- count requests served entirely from Cloudflare cache.

Cloudflare edge-log ingestion, historical backfill, and richer user-agent
classification are optional future work, not prerequisites for this design.
