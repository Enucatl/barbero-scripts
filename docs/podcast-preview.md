# Private podcast preview

This is an unlisted preview, not authentication: anyone with the URL can use or share it. Do not
submit this feed to Apple or other directories until redistribution rights have been confirmed.

## Publish

Create a URL-safe random token and keep it outside Git:

```bash
openssl rand -base64 32 | tr '+/' '_-' | tr -d '=' > .podcast-preview-token
uv run barbero publish-preview
```

The command validates metadata and source renders, encodes Opus to 48 kHz MP3 (96 kbps mono or
160 kbps stereo), and atomically replaces only
`/scratch/archive/barbero-english/published/<token>`. The feed URL is
`https://podcast.enucatl.com/<token>/feed.xml`. In AntennaPod, choose **Add podcast → RSS address**
and paste that URL.

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

To rotate the preview URL, replace `.podcast-preview-token`, rerun publication, verify the new
feed, and remove the old token directory only after subscribers have migrated.

## Rights-gated public launch

Before public launch, confirm redistribution rights, export fresh MP3/AAC delivery masters from
Reaper instead of transcoding Opus, and publish them at stable public URLs while retaining the
UUID5 GUIDs. Remove no-index controls, validate the public feed and media delivery, and only then
submit it through Apple Podcasts Connect and confirm rights to all third-party material.
