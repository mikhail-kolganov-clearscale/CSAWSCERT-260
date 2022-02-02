# CloudFormation templates
## cfn_stacks/VPC.yaml
Creating a VPC with several Public Subnets and IGW
## cfn_stacks/ECS.yaml
ECS cluster with basic Task definition and Service
## cfn_stacks/CICD.yaml
CodeBuild project and CodePipeline to track updates of the CodeCommit repo and update the Task container image


## ./https_server.py
A simple python script. Reads the './test.html' file and runs simpleHTTPserver

## ./Dockerfile
Container build file for creating an image

## ./buildspec.yml
CodeBuild workflow scenario for building a docker image and pushing it to the ECR