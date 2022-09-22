FROM alpine:latest AS terraform_stage

ARG TF_CLI_VERSION
ENV TF_CLI_VERSION=$TF_CLI_VERSION

WORKDIR /opt

RUN apk update && apk add wget unzip \
  && wget https://releases.hashicorp.com/terraform/${TF_CLI_VERSION}/terraform_${TF_CLI_VERSION}_linux_amd64.zip \
  && unzip terraform_${TF_CLI_VERSION}_linux_amd64.zip

FROM python:alpine AS development_build_stage

WORKDIR /opt

RUN python -m venv venv

ENV PATH=/opt/venv/bin:$PATH

WORKDIR /opt/src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN pip install .

FROM python:alpine AS test_stage

WORKDIR /opt

ARG TF_CLI_VERSION
ENV TF_CLI_VERSION=$TF_CLI_VERSION

COPY --from=terraform_stage /opt/terraform /usr/local/bin/terraform

COPY --from=development_build_stage /opt/venv /opt/venv

ENV PATH=/opt/venv/bin:$PATH

WORKDIR /opt/src

COPY . .

RUN cd artifacts && terraform init && terraform validate \
  && terraform plan -out terraform-v${TF_CLI_VERSION}.tfplan.test \
  && terraform apply -auto-approve \
  && cp terraform.tfstate terraform-v${TF_CLI_VERSION}.tfstate.test

RUN TF_CLI_CHDIR=/opt/src/artifacts coverage run -m pytest

FROM python:alpine AS build_stage

WORKDIR /opt

RUN python -m venv venv

ENV PATH=/opt/venv/bin:$PATH

WORKDIR /opt/src

COPY . .

RUN pip install .

FROM python:alpine AS final_stage

LABEL maintainer="Saeid Bostandoust <hello@tf2project.io>"

COPY --from=terraform_stage /opt/terraform /usr/local/bin/terraform

COPY --from=build_stage /opt/venv /opt/venv

ENV PATH=/opt/venv/bin:$PATH

ENTRYPOINT ["python"]

CMD ["-c", "import tf2; print(tf2.__version__)"]
