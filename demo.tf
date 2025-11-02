provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "bad" {
  bucket = "my-public-bucket"
  acl    = "public-read"
}
