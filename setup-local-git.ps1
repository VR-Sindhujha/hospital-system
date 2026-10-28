# Run this script in PowerShell from the extracted hospital-system-offline-pack folder.
# It creates three branches with each version's files at the repository root.
$ErrorActionPreference = 'Stop'

# Confirm Git is available before proceeding.
git --version

# Initialize the repository if it has not already been initialized.
if (-not (Test-Path '.git')) { git init }
git config user.name "Your Name"
git config user.email "you@example.com"

# Prepare v1 files at repository root.
Copy-Item v1\* . -Force
Copy-Item v1\.gitignore . -Force
Copy-Item v1\.dockerignore . -Force
git add app.py test_app.py requirements.txt Dockerfile Jenkinsfile k8s-deployment.yaml .gitignore .dockerignore
git commit -m "v1: add patient registration"
git branch -M v1

# Create v2 branch and replace root files with v2 version.
git switch -c v2
Copy-Item v2\* . -Force
Copy-Item v2\.gitignore . -Force
Copy-Item v2\.dockerignore . -Force
git add app.py test_app.py requirements.txt Dockerfile Jenkinsfile k8s-deployment.yaml .gitignore .dockerignore
git commit -m "v2: add patient listing"

# Create v3 branch and replace root files with v3 version.
git switch -c v3
Copy-Item v3\* . -Force
Copy-Item v3\.gitignore . -Force
Copy-Item v3\.dockerignore . -Force
git add app.py test_app.py requirements.txt Dockerfile Jenkinsfile k8s-deployment.yaml .gitignore .dockerignore
git commit -m "v3: add patient deletion"

git log --oneline --decorate --all
Write-Host "Local v1, v2, v3 branches created. Do not run the push commands until the network is available."
