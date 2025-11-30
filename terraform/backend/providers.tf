provider "aws" {
  region                      = "us-east-1"
  skip_credentials_validation = true
  skip_requesting_account_id  = true
  dynamic "endpoints" {
    for_each = terraform.workspace == "localstack" ? [1] : [0]
    content {
      s3 = local.config.infrastructure.localstack_endpoint
    }
  }
}

