terraform {
  required_version = ">= 1.5.0"

  backend "s3" {
    bucket  = "m6freeman.sh-terraform-state"
    key     = "m6freeman.sh/terraform.tfstate"
    region  = "us-east-1"
    encrypt = true
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.19.0"
    }
  }
}
