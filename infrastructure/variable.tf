variable "aws-region" {
  default="us-east-2"
}
variable "lambda_function_name" {
  default = "IGTIExecutaEMRaovivo"
}
variable "key_pair_name" {
  default = "guerreiro-igti-teste"
}

variable "airflow_subnet_id" {
  default = "subnet-fcc65397"
}

variable "vpc_id" {
  default = "vpc-772a471c"
}
