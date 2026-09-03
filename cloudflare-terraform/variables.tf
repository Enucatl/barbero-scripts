variable "cloudflare_api_token" {
  description = "Cloudflare token with tunnel, DNS, and Cache Rules edit permissions."
  type        = string
  sensitive   = true
}

variable "account_id" {
  type = string
}

variable "zone_id" {
  type = string
}

variable "hostname" {
  type    = string
  default = "podcast.enucatl.com"
}
