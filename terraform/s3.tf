
resource "aws_s3_bucket" "website_bucket" {
  bucket        = local.config.infrastructure.s3.website
  force_destroy = true
}

resource "aws_s3_bucket_public_access_block" "website_bucket" {
  bucket = aws_s3_bucket.website_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_object" "upload_object" {
  bucket       = aws_s3_bucket.website_bucket.id
  key          = each.value
  source       = "../dist/${each.value}"
  etag         = filemd5("../dist/${each.value}")
  for_each     = fileset("../dist/", "*")
  content_type = "text/html"
}

resource "aws_s3_bucket_website_configuration" "website_bucket" {
  bucket = aws_s3_bucket.website_bucket.id

  index_document {
    suffix = "index"
  }

  error_document {
    key = "error"
  }
}

resource "aws_s3_bucket_policy" "website_bucket" {
  depends_on = [aws_s3_bucket_public_access_block.website_bucket]
  bucket     = aws_s3_bucket.website_bucket.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Sid       = "CloudfrontPublicReadGetObject"
        Effect    = "Allow"
        Principal = { "AWS" : "cloudfront.amazonaws.com" }
        Action    = "s3:GetObject"
        Resource  = "${aws_s3_bucket.website_bucket.arn}/*"
        Condition = {
          StringEquals = {
            "AWS:SourceArn" : aws_cloudfront_distribution.s3_distribution.arn
          }
        }
      }
    ]
  })
}
