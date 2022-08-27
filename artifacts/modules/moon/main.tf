variable "test_input" {
  type = string
}

resource "local_file" "test" {
  filename = "moon.log"
  content  = var.test_input
}

output "test_output" {
  value = local_file.test.filename
}
