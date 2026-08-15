resource "cloudflare_zero_trust_tunnel_cloudflared" "podcast" {
  account_id = var.account_id
  name       = "barbero-english-podcast"
  config_src = "cloudflare"
}

data "cloudflare_zero_trust_tunnel_cloudflared_token" "podcast" {
  account_id = var.account_id
  tunnel_id  = cloudflare_zero_trust_tunnel_cloudflared.podcast.id
}

resource "cloudflare_dns_record" "podcast" {
  zone_id = var.zone_id
  name    = var.hostname
  content = "${cloudflare_zero_trust_tunnel_cloudflared.podcast.id}.cfargotunnel.com"
  type    = "CNAME"
  ttl     = 1
  proxied = true
}

resource "cloudflare_zero_trust_tunnel_cloudflared_config" "podcast" {
  account_id = var.account_id
  tunnel_id  = cloudflare_zero_trust_tunnel_cloudflared.podcast.id
  source     = "cloudflare"
  config = {
    ingress = [
      {
        hostname = var.hostname
        service  = "http://caddy:8080"
      },
      {
        service = "http_status:404"
      }
    ]
  }
}

output "tunnel_token" {
  value     = data.cloudflare_zero_trust_tunnel_cloudflared_token.podcast.token
  sensitive = true
}
