variable "test_number" {
  type    = number
  default = 10
}

variable "test_string" {
  type    = string
  default = "test"
}

variable "test_boolean" {
  type    = bool
  default = true
}

variable "test_list" {
  type    = list(string)
  default = ["test1", "test2"]
}

variable "test_object" {
  type = object({
    testkey = string
  })
  default = {
    "testkey" = "testvalue"
  }
}

variable "test_for_each" {
  type = map(string)
  default = {
    "test_for_each1" = "test",
    "test_for_each2" = "test"
  }
}

data "local_file" "test_data_resource" {
  filename = "testdata.txt"
}

resource "null_resource" "test1" {}
resource "null_resource" "test2" {}

resource "null_resource" "test_count" {
  count = 2
}

resource "null_resource" "test_for_each" {
  for_each = var.test_for_each
}

resource "random_integer" "test_number" {
  min = 10
  max = 20
}

resource "random_string" "test_string" {
  length = 8
}

resource "random_password" "test_password" {
  length = 8
}

resource "local_file" "test1" {
  filename = "test1.log"
  content  = "Test 1 from Terraform"
}

resource "local_file" "test2" {
  filename = "test2.log"
  content  = "Test 2 from Terraform"
}

module "test_earth" {
  source     = "./modules/earth"
  test_input = "Hello Earth"
}

module "test_moon" {
  source     = "./modules/moon"
  test_input = "Hello Moon"
}

output "test_number" {
  value = var.test_number
}

output "test_string" {
  value = var.test_string
}

output "test_boolean" {
  value = var.test_boolean
}

output "test_list" {
  value = var.test_list
}

output "test_object" {
  value = var.test_object
}

output "test_password" {
  value     = random_password.test_password.result
  sensitive = true
}

output "test_earth_output" {
  value = module.test_earth.test_output
}

output "test_moon_output" {
  value = module.test_moon.test_output
}
