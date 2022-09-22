#!/usr/bin/bash

# Terraform Test Framework
# https://github.com/tf2project/tf2project

if [[ -z "$TF_CLI_VERSION" ]]; then
    read -p "Enter Terraform CLI version: " TF_CLI_VERSION
fi

docker build --build-arg TF_CLI_VERSION=$TF_CLI_VERSION -t tf2project/tf2project:latest .

LAST_GIT_COMMIT=$(git rev-parse HEAD | xargs)

docker tag tf2project/tf2project:latest tf2project/tf2project:$LAST_GIT_COMMIT

LAST_GIT_TAG=$(git tag --points-at HEAD | xargs)

if [[ ! -z "$LAST_GIT_TAG" ]]; then
    docker tag tf2project/tf2project:latest tf2project/tf2project:$LAST_GIT_TAG
fi
