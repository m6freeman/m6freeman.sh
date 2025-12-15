
resource "aws_route53_zone" "my_domain" {
  name = "${local.config.infrastructure.s3.website}."
}

resource "aws_route53_record" "www" {
  for_each = {
    main = local.config.infrastructure.s3.website
    www  = "www.${local.config.infrastructure.s3.website}"
  }

  zone_id = aws_route53_zone.my_domain.zone_id
  name    = each.value
  type    = "A"

  alias {
    name                   = aws_cloudfront_distribution.s3_distribution.domain_name
    zone_id                = aws_cloudfront_distribution.s3_distribution.hosted_zone_id
    evaluate_target_health = true
  }
}
