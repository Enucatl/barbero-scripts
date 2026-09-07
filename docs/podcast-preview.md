# Podcast publication

The public podcast is served from `https://podcast.enucatl.com/`. Publish only after redistribution
rights have been confirmed.

## Public publication

Build the public tree without a URL token:

```bash
uv run barbero publish-preview --public
```

This atomically replaces `/scratch/archive/barbero-english/published` with the root publication,
including `feed.xml`, `index.html`, episode pages, and MP3 files. Caddy serves only that public
tree. Old token-prefixed preview URLs are not redirected or served.

The Cloudflare cache bypass for `podcast.enucatl.com` must be applied before publication so all
content requests reach Caddy and are logged to Loki.

Verify the root feed and page before announcing the podcast:

```bash
curl -I https://podcast.enucatl.com/feed.xml
curl -I https://podcast.enucatl.com/
```

Both should reach Caddy and return successful responses. Verify an MP3 URL from the feed and check
the corresponding Caddy request in Loki.

## Private preview

The tokenized preview command still writes an unlisted tree under
`/scratch/archive/barbero-english/published/<token>`. Caddy does not serve that prefix; use
`--public` when the origin should be reachable.

## Publish

Create a URL-safe random token and keep it outside Git:

```bash
openssl rand -base64 32 | tr '+/' '_-' | tr -d '=' > .podcast-preview-token
uv run barbero publish-preview
```

The command validates metadata and source renders, encodes Opus to 48 kHz MP3 (96 kbps mono or
160 kbps stereo), and atomically replaces only
`/scratch/archive/barbero-english/published/<token>`. That tree is not served by Caddy.

## Deploy

Create the tunnel and DNS record, then store its sensitive output as the Compose secret:

```bash
cd cloudflare-terraform
terraform init
terraform apply
mkdir -p ../secrets
terraform output -raw tunnel_token > ../secrets/cloudflare-tunnel-token
chmod 600 ../secrets/cloudflare-tunnel-token
cd ..
docker compose config
docker compose up -d
```

Supply `cloudflare_api_token`, `account_id`, and `zone_id` through ignored `.tfvars` or
`TF_VAR_*`. The origin exposes only generated HTML, RSS, artwork, transcript pages, and hashed
MP3s. Caddy supplies content lengths, HEAD handling, and byte ranges; raw project/audio files are
not mounted.

Puppet node data grants read access only to container root on this host, where Docker
user-namespace remapping maps container UID 0 to host UID 100000.

To rotate a leftover preview directory, remove the old token directory only after you no longer
need those files.

## Rights-gated public launch

Before public launch, confirm redistribution rights, export fresh MP3/AAC delivery masters from
Reaper instead of transcoding Opus, and publish them at stable public URLs while retaining the
UUID5 GUIDs. Remove no-index controls, validate the public feed and media delivery, and only then
submit it through Apple Podcasts Connect and confirm rights to all third-party material.
