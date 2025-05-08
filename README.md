# Gym Membership Web App with CI/CD Pipeline

This project implements a complete DevOps pipeline for a Gym Membership Web Application using Flask, Docker, Jenkins, and AWS.

## Project Structure

```
.
├── app/
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── register.html
│   │   └── contact.html
│   │
│   ├── app.py
│   └── requirements.txt
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
├── Dockerfile
│
├── Jenkinsfile
│
└── README.md
```

## Prerequisites

- AWS Account with appropriate credentials
- Docker Hub account
- Jenkins server
- Git

## Setup Instructions

### 1. AWS Infrastructure Setup

1. Navigate to the terraform directory:
   ```bash
   cd terraform
   ```

2. Initialize Terraform:
   ```bash
   terraform init
   ```

3. Create a `terraform.tfvars` file with your variables:
   ```hcl
   aws_region = "us-east-1"
   key_name   = "your-ssh-key-name"
   ```

4. Apply the Terraform configuration:
   ```bash
   terraform apply
   ```

### 2. Jenkins Setup

1. Install Jenkins on the EC2 instance:
   ```bash
   sudo yum update -y
   sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
   sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.key
   sudo yum install jenkins -y
   sudo systemctl start jenkins
   sudo systemctl enable jenkins
   ```

2. Configure Jenkins:
   - Access Jenkins at `http://<ec2-public-ip>:8080`
   - Install suggested plugins
   - Create a new pipeline job
   - Configure the pipeline to use the Jenkinsfile from SCM

3. Add credentials in Jenkins:
   - Docker Hub credentials (ID: docker-hub-credentials)
   - SSH key for EC2 access (ID: ec2-ssh-key)

### 3. Application Deployment

1. Push your code to a Git repository:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. Configure the Jenkins pipeline with your repository URL

3. Run the pipeline to deploy the application

## Features

- Modern, responsive web interface
- Membership package display
- Trainer information
- Registration form
- Contact form
- Automated CI/CD pipeline
- Containerized deployment
- Infrastructure as Code (IaC)

## Security Considerations

- The security group allows access to ports 22, 80, and 8080
- IAM roles are configured with least privilege principle
- Docker images are scanned for vulnerabilities
- Jenkins credentials are securely stored

## Maintenance

- Monitor Jenkins pipeline execution
- Regularly update dependencies
- Check AWS CloudWatch for instance metrics
- Review security group rules periodically

## Troubleshooting

1. If the application is not accessible:
   - Check EC2 instance status
   - Verify security group rules
   - Check Docker container logs

2. If Jenkins pipeline fails:
   - Review Jenkins console output
   - Verify credentials configuration
   - Check Docker Hub access

## License

This project is licensed under the MIT License. 