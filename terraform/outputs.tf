output "public_zone_name_servers" {
  description = "Name‑servers that must be set at the registrar"
  value       = aws_route53_zone.my_domain.name_servers
}

output "cloudfront_distribution_domain_name" {
  description = "The domain name of the CloudFront distribution"
  value       = aws_cloudfront_distribution.s3_distribution.domain_name
}
