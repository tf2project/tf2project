# Terraform Test Framework

<p align="center">
  <img src="https://raw.githubusercontent.com/tf2project/tf2project/master/logo.png" alt="Terraform Test Framework">
</p>

<p align="center">Unified Test Framework to test Terraform codes and Terraform-provisioned infrastructures.</p>

<p align="center">
<strong>The new version, v0.2.0 (Freedom) is now available.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/github/last-commit/tf2project/tf2project" alt="GitHub last commit">
  <a href="https://github.com/tf2project/tf2project/blob/master/LICENSE" target="_blank"><img src="https://img.shields.io/github/license/tf2project/tf2project" alt="GitHub license"></a>
  <a href="https://github.com/tf2project/tf2project/stargazers" target="_blank"><img src="https://img.shields.io/github/stars/tf2project/tf2project" alt="GitHub stars"></a>
  <a href="https://github.com/tf2project/tf2project/network" target="_blank"><img src="https://img.shields.io/github/forks/tf2project/tf2project" alt="GitHub forks"></a>
  <a href="https://github.com/tf2project/tf2project/issues" target="_blank"><img src="https://img.shields.io/github/issues/tf2project/tf2project" alt="GitHub issues"></a>
</p>

---

**Documentation:** <a href="https://tf2project.io" target="_blank">https://tf2project.io</a>

**Source Code:** <a href="https://github.com/tf2project/tf2project" target="_blank">https://github.com/tf2project/tf2project</a>

**Changelog:** <a href="https://tf2project.io/changelog.html" target="_blank">https://tf2project.io/changelog.html</a>

---

**TF2** is a unified test framework to test Terraform codes and Terraform-provisioned infrastructures. With TF2, you can implement PaC(**Policy as Code**), **Compliance** tests and e2e(**End to End**) tests just in a unified framework.

## Requirements

The **TF2 core** doesn't have any external or third-party requirements, and we will keep this approach as the main development policy to reduce the attack surface. This policy is created because you run the TF2 in your critical environments, CI/CD systems, and cloud/on-premises infrastructures, and we want to keep you completely secure. The TF2 core is just using standard and official Python libraries.

## Installation

On **production** environment:

```bash
pip install tf2project
```

On **development** environment:

```bash
export ENV=development
pip install git+https://github.com/tf2project/tf2project
```

## Docker Image

You can also use our official Docker image to run the framework. The image `tf2project/tf2project` consists of the latest version of Terraform and the TF2 framework itself.

It's a ready-to-go image to integrate the TF2 within CI/CD pipelines.

```bash
docker run tf2project/tf2project:latest
```

## License

This project is licensed under the terms of the Apache 2.0 license.

Copyright &copy; 2022 Saeid Bostandoust
