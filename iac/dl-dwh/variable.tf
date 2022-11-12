locals {
  project_id             = replace(var.project_id, "-", "_")
  data_lake_bucket       = "${local.project_id}_dt-lake"
  bigquery_dataset       = "${local.project_id}_bq_data"
}

variable "project_name" {
  description = "Your GCP Project Name"
  default     = "itv-hub-programme"
  type        = string
}

variable "project_id" {
  description = "Your GCP Project ID"
  default     = "project_id number"
  type        = string
}

variable "state_bucket" {
  description = "Bucket name for storing terrafrom state and lock files"
  default     = "state-bucket name"
  type        = string
}

variable "region" {
  description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
  default     = "europe-west6"
  type        = string
}

variable "storage_class" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default     = "STANDARD"
  type        = string
}