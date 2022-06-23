# tf2

![Visits Badge](https://badges.pufler.dev/visits/ssbostan/tf2)
![GitHub last commit](https://img.shields.io/github/last-commit/ssbostan/tf2)
[![GitHub license](https://img.shields.io/github/license/ssbostan/tf2)](https://github.com/ssbostan/tf2/blob/master/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/ssbostan/tf2)](https://github.com/ssbostan/tf2/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ssbostan/tf2)](https://github.com/ssbostan/tf2/network)
[![GitHub issues](https://img.shields.io/github/issues/ssbostan/tf2)](https://github.com/ssbostan/tf2/issues)

**T**erra**f**orm  **T**est **F**ramework aka **Tf2** is a python framework to test Terraform provisioned resources.

## What does Tf2 intend to solve?

In real-world, real teams, real infrastructures, enterprises or somewhere else, everything can destroy in a jiffy. Why? You tested your Terraform codes before deployment(unit test, integration test, validation test, etc.), but your infrastructure that is provisioned by Terraform is not working properly. Your codes are correct, but something goes wrong because of bad configuration, miss-configuration, bad dependency management of resources, miss-deploying of some resources, etc. What if you had such a way to test your Terraform resources and their behaviour after applying them to the real infrastructures? Here you go! Tf2 is here to solve this concern by connecting to the real infrastructure, testing Terraform provisioned resources and their behaviours and comparing them to your specified desired state. With the aid of Tf2, you can test your real Terraform results in your test environment and if everything went good, apply your changes to your production environment.
