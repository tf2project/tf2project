#!/usr/bin/bash

# Terraform Test Framework
# https://github.com/tf2project/tf2project

if [[ -z "$TF_CLI_VERSION" ]]; then
    read -p "Enter Terraform CLI version: " TF_CLI_VERSION
fi

PROJECT_WORKDIR=$(pwd)

export TF_CLI_VERSION=$TF_CLI_VERSION

cd artifacts && terraform init && terraform validate \
  && terraform plan -out terraform-v$TF_CLI_VERSION.tfplan.test \
  && terraform apply -auto-approve \
  && cp terraform.tfstate terraform-v$TF_CLI_VERSION.tfstate.test \
  && terraform destroy -auto-approve

export TF_CLI_CHDIR="$PROJECT_WORKDIR/artifacts"

cd $PROJECT_WORKDIR

coverage run -m pytest
coverage html
coverage xml

rm -rf artifacts/terraform* .tf2result
