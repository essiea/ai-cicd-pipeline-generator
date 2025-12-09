# ⚙️ AI CI/CD Pipeline Generator (AWS Bedrock)

![CI](https://github.com/essiea/ai-cicd-pipeline-generator/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-orange)
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC)
![License](https://img.shields.io/badge/License-MIT-green)

The **AI CI/CD Pipeline Generator** creates CI/CD pipelines, Terraform IaC, or Kubernetes manifests from natural language + JSON specifications using Claude 3 Sonnet (Bedrock).

---

## 🚀 Features

- Generate GitHub Actions YAML  
- Generate Terraform templates  
- Generate Kubernetes deployments  
- API Gateway endpoint  
- Serverless Lambda execution  
- Fast, low cost  

---

## 🧠 Architecture

\`\`\`mermaid
flowchart TD
    U[User / CLI] --> API[API Gateway]
    API --> L[Lambda Pipeline Generator]
    L --> B[Bedrock Claude 3 Sonnet]
    B --> L
    L --> OUT[Generated Pipeline YAML]
\`\`\`

---

## 🤝 Contributing  
PRs welcome.

---

## 📄 License  
MIT License.
