from datetime import datetime,timedelta
import os

#Define the furthest date want to analyze
date_stop = (datetime.today() - timedelta(days=7)) #In this example, we analyze the last 7 days

#Where the results are stored
folder = os.environ.get('VOLUME_FOLDER')

#The categories to tag your websites
categories = {
    "Programming and Development": [
        "software development", "programming", "coding", "scripting",
        "algorithm", "data structure", "backend", "frontend",
        "API", "microservices", "containerization", "cloud-native", "k8s", "kubernetes"
    ],
    "Emerging Technologies": [
        "artificial intelligence", "machine learning", "deep learning",
        "big data", "data-driven", "blockchain", "decentralized",
        "edge computing", "serverless", "IoT", "ai", "ia"
    ],
    "Cloud and Infrastructure": [
        "cloud computing", "AWS", "Azure", "Google Cloud", "Kubernetes",
        "virtualization", "infrastructure as code", "DevOps",
        "continuous integration", "continuous delivery", "CI/CD", "ci", "cd",
        "scalability", "resiliency"
    ],
    "Software Architecture and Practices": [
        "design patterns", "agile development", "scrum", "kanban",
        "code review", "refactoring", "technical debt",
        "performance optimization", "test automation", "unit testing", "solid"
    ],
    "Security and Compliance": [
        "cybersecurity", "data privacy", "encryption", "authentication",
        "authorization", "vulnerability management", "zero trust",
        "compliance", "GDPR", "SOC", "owasp", "malware"
    ],
    "Data and Analytics": [
        "data pipeline", "ETL", "data visualization", "business intelligence",
        "analytics", "data lake", "data warehouse", "real-time processing",
        "predictive analytics"
    ],
    "Career and Trends": [
        "emerging technologies", "industry trends", "tech forecast",
        "developer tools", "open source", "productivity tools",
        "programming languages", "software engineering practices"
    ],
    "Other Topics": [
        "performance tuning", "debugging", "version control", "git",
        "collaboration tools", "developer productivity", "software testing",
        "IT infrastructure", "automation", "distributed systems"
    ]
}

#The url to access Ollama Container
ollama_url = os.environ.get('OLLAMA_BASE_URL')