locals {
  config       = jsondecode(file("${path.module}/../config/config.json"))
  s3_origin_id = "s3-${aws_s3_bucket.website_bucket.id}"
}

