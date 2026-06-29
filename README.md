# LogiHaul AWS Cloud Practitioner Capstone

## Overview

This repository contains the design, implementation, and documentation for the **LogiHaul AWS Cloud Engineering Capstone Project**.

LogiHaul is a pan-Nigeria logistics platform that enables customers to place delivery requests, assigns drivers, tracks deliveries in real time, and sends automated notifications. The solution is designed on Amazon Web Services (AWS) using cloud-native services that provide scalability, high availability, security, monitoring, and cost optimisation.

The architecture was designed to satisfy the following business requirements:

* Support over 5,000 truck drivers operating across Nigeria.
* Handle unpredictable traffic spikes of up to 50×.
* Confirm deliveries in under 2 seconds.
* Survive an Availability Zone (AZ) failure without data loss.
* Maintain operational costs below **$150/month** during normal operations and below **$400/month** during peak demand.

---

# Project Objectives

The project demonstrates the practical application of AWS Cloud Engineering concepts through the design and implementation of a production-style cloud solution.

Objectives include:

* Build a secure AWS environment.
* Implement high availability using Multi-AZ architecture.
* Deploy scalable compute resources.
* Design resilient storage and database solutions.
* Build an event-driven notification system.
* Monitor workloads using Amazon CloudWatch.
* Apply AWS security best practices.
* Optimise infrastructure costs.

---

# Business Requirements

The solution must:

* Process customer delivery requests.
* Assign drivers efficiently.
* Store delivery records securely.
* Provide automated email notifications.
* Scale automatically during heavy demand.
* Recover from infrastructure failures.
* Protect customer and business data.

---

# AWS Services Used

## Networking

* Amazon VPC
* Internet Gateway
* NAT Gateway
* Route Tables
* Security Groups
* Network ACLs

## Compute

* Amazon EC2
* Launch Template
* Auto Scaling Group
* Application Load Balancer

## Storage

* Amazon S3

## Databases

* Amazon DynamoDB
* Amazon RDS (MySQL)

## Serverless

* AWS Lambda
* Amazon API Gateway

## Messaging

* Amazon SQS
* Amazon SNS

## Monitoring

* Amazon CloudWatch
* CloudWatch Logs
* CloudWatch Alarms

## Security

* AWS IAM
* AWS KMS
* AWS CloudTrail

---

# AWS Architecture

<img width="1536" height="1024" alt="LogiHaul Architecture Diagram" src="https://github.com/user-attachments/assets/74a92875-72ba-4cf0-830c-ee15ddc38b31" />


```
Customer
    │
    ▼
Application Load Balancer
    │
    ▼
Auto Scaling Group (EC2)
    │
 ┌──┴──────────────┐
 │                 │
 ▼                 ▼
DynamoDB        Amazon RDS

    │
    ▼
API Gateway
    │
    ▼
Lambda
    │
    ▼
Amazon SQS
    │
    ▼
Lambda
    │
    ▼
Amazon SNS
    │
    ▼
Email Notification
```

---

# Architecture Layers

## Layer 1 – Foundation

* Custom VPC
* Public and Private Subnets
* Route Tables
* Internet Gateway
* NAT Gateway
* Bastion Host

## Layer 2 – Compute

* EC2 Web Servers
* Launch Template
* Auto Scaling Group
* Application Load Balancer

## Layer 3 – Storage

* Amazon S3
* Versioning
* Lifecycle Policy
* Server-side Encryption
* Cross-Region Replication

## Layer 4 – Database

### Amazon RDS

Stores billing information.

### Amazon DynamoDB

Stores logistics and delivery information.

### ElastiCache (Production Recommendation)

Caches frequently accessed data to reduce database load and improve response times.

---

## Layer 5 – Serverless

* API Gateway
* Lambda Functions
* Amazon SQS
* Amazon SNS

---

## Layer 6 – Monitoring

* CloudWatch Dashboard
* CloudWatch Logs
* CloudWatch Alarms
* Logs Insights

---

# Handling the 50× Traffic Spike

The solution supports sudden increases in traffic through:

* Auto Scaling Group dynamically launching additional EC2 instances.
* Application Load Balancer distributing requests across healthy instances.
* DynamoDB On-Demand Capacity automatically scaling read and write throughput.
* Amazon SQS buffering requests during traffic surges.
* Reserved Lambda Concurrency ensuring notification processing capacity.

Together, these services enable the platform to absorb large traffic spikes without manual intervention.

---

# High Availability

The production architecture provides high availability by:

* Deploying resources across two Availability Zones.
* Using an Application Load Balancer.
* Auto Scaling Group health checks.
* Multi-AZ Amazon RDS (production design).
* Cross-Region S3 replication.
* Stateless application servers.

---

# Security Implementation

Security controls include:

* IAM Least Privilege
* Security Groups
* Private Subnets
* Encryption at Rest
* Encryption in Transit
* AWS KMS
* CloudTrail Logging
* Secrets Manager (production recommendation)

---

# Monitoring and Logging

The environment is monitored using:

* CloudWatch Dashboards
* CloudWatch Metrics
* CloudWatch Alarms
* CloudWatch Logs
* CloudWatch Logs Insights

Monitoring enables proactive detection of performance issues and operational failures.

---

# Cost Optimisation

The architecture incorporates several AWS cost optimisation strategies:

* Auto Scaling to match demand.
* DynamoDB On-Demand Capacity.
* S3 Lifecycle Policies.
* Serverless computing with AWS Lambda.
* Right-sized EC2 instances.
* Storage lifecycle management.

Estimated operating cost:

* Steady State: **< $150/month**
* Peak Demand: **< $400/month**

---

# Project Structure

```
docs/
diagrams/
lambda/
policies/
templates/
user-data/
evidence/
assets/
README.md
LICENSE
```

---

# Testing Performed

The following components were successfully tested:

* VPC Connectivity
* EC2 Deployment
* Auto Scaling
* Application Load Balancer
* RDS Connectivity
* DynamoDB Operations
* S3 Uploads
* Lambda Invocation
* API Gateway POST Requests
* Amazon SQS Messaging
* Amazon SNS Email Notifications
* CloudWatch Monitoring
* CloudWatch Alarms

---

# Screenshots

<img width="1918" height="1078" alt="Screenshot 2026-06-29 133645" src="https://github.com/user-attachments/assets/17d2abda-4750-4c81-bf6e-19b33197cee1" />

<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/ce2d5ea4-36b2-4e18-97f5-5957f38b9fcc" />

<img width="1918" height="1078" alt="Screenshot 2026-06-29 141037" src="https://github.com/user-attachments/assets/1b6e8ed1-c703-49a8-8861-02231368993c" />

<img width="1918" height="1078" alt="Screenshot 2026-06-26 220120" src="https://github.com/user-attachments/assets/82b713a8-aeb9-4512-b568-9a944302f944" />

<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/e9ea24ef-213f-4baf-8456-6bcf62ff900c" />

<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/5287e127-f892-4123-8319-a97cf535672a" />

<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/f832147f-0e1f-4c81-9553-e6e2498955ff" />

<img width="1918" height="1078" alt="image" src="https://github.com/user-attachments/assets/5b82d417-4679-4e03-be51-6c344e343156" />

<img width="1918" height="1078" alt="Screenshot 2026-06-29 184540" src="https://github.com/user-attachments/assets/b99322e0-09ab-4f82-b4dc-5f293e960259" />

<img width="1918" height="1078" alt="Screenshot 2026-06-29 123444" src="https://github.com/user-attachments/assets/97052b9a-071b-4ffa-9bcf-f33974a0137f" />

---

# Future Improvements

Potential enhancements include:

* Amazon ECS or EKS deployment.
* AWS WAF integration.
* AWS Shield Advanced.
* AWS X-Ray.
* Amazon ElastiCache implementation.
* CI/CD using GitHub Actions and AWS CodePipeline.

---

# References

* AWS Documentation
* AWS Well-Architected Framework
* AWS Pricing Calculator

---

# Author

**Emmanuel Idebuemi**

AWS Cloud Engineering Capstone Project

2026
