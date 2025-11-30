# Local and Remote Deployment Template

- Provisioner
    - Github Actions
- Orchestrator
    - Terraform
- Provider
    - AWS
    - LocalStack

## What you get out of the box

This template provides a minimally configured, customizable, CI pipeline to begin deploying projects to LocalStack and AWS using the same Github Actions Workflow.

The template's Terraform infrastructure demonstrates the orchestration of a static s3 hosted website. Project source code files should be stored in `src/` and deployment artifacts in `dist/`.

## Why would you use this pattern?

- You want to wrestle with testing new infrastructure in a locally controlled, sanatized environment without deploying directly to a remote cloud provider
- You need to test deployed changes during a remote cloud provider outage
- You desire a more homogenous local and remote development and deployment experience

## Requirements

- [act](https://github.com/nektos/act) is installed
- [docker](https://www.docker.com/) is installed
- [localstack](https://github.com/localstack/localstack) is running within a separate container on the local host machine

## Optional 

> **Note:** These are not required to run the deployment, but are very handy when developing locally

- [awscli](https://github.com/aws/aws-cli)
- [awscli-local](https://github.com/localstack/awscli-local) is installed (probably via pip)
- [terraform](https://github.com/hashicorp/terraform)
- [terraform-local](https://github.com/localstack/terraform-local) is installed (probably via pip)

## Assumptions and Opinions

- This template assumes the terraform infra will hook into an already existing s3 backend. If it is not found by the name provided in `config/config.json`, it will create one by that name in LocalStack only and will exit in production.
- Github Actions and Terraform both leverage the shared configuration file in `config/config.json`
- LocalStack deployments are triggered by manually via a workflow_dispatch of the `deploy` job. This is customizable by changing the expression found in Job: `deploy` Step: `Set USING_LOCALSTACK Variable`

## Example

``` bash
cd project_template
localstack start -d
act workflow_dispatch -j deploy
curl localhost:4566/website-bucket/index.html
#  Index page from s3!
```
