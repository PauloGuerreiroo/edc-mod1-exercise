provider "aws" {
  region = "us-east-2"
}
terraform {
  backend "s3" {
    bucket = "terraform-state-igti-pauloguerreiro"
    key = "state/igti/edc/mod1/terraform.tfstate"
    region = "us-east-2"
  }
}