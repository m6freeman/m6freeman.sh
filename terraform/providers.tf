provider "aws" {
  region = local.config.project.region
  # dynamic "endpoints" {
  # for_each = terraform.workspace == "localstack" ? [1] : [0]
  # content {
  # s3  = local.config.infrastructure.localstack_endpoint
  # sts = local.config.infrastructure.localstack_endpoint
  # }
  # }
  skip_credentials_validation = terraform.workspace == "localstack"
  skip_requesting_account_id  = terraform.workspace == "localstack"
}
