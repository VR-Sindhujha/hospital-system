HOSPITAL SYSTEM — OFFLINE-FIRST PROJECT PACK
============================================

Assigned features:
  v1: Add Patient
  v2: View — display patient list
  v3: Delete — remove patient record

CONTENTS
  v1/, v2/, v3/ each contain app.py, test_app.py, requirements.txt, Dockerfile, Jenkinsfile, .gitignore, .dockerignore, k8s-deployment.yaml.
  setup-local-git.ps1 creates v1/v2/v3 Git branches with each version's files at the repository root, which is the layout Jenkins expects.

BEFORE USING
1. Replace YOUR_DOCKERHUB_USERNAME in each Jenkinsfile and k8s-deployment.yaml with your Docker Hub username.
2. Edit setup-local-git.ps1 and replace "Your Name" and "you@example.com" with your Git identity.
3. This pack is prepared for a Windows Jenkins agent because the lab examples use `bat`.
4. The app stores patient records in memory. Records disappear when the app/pod restarts. This is a simple lab demonstration, not a production medical system.
5. Internet disconnection means GitHub/Docker Hub pushes and uncached dependency/base-image downloads may fail. Prepare locally now; push when connectivity is restored.

LOCAL TEST (run inside one version folder, e.g. v1):
  python --version
  python -m pip --version
  python -m pip show Flask
  python -m pip install -r requirements.txt
  python -m unittest -v
  python app.py

In another terminal:
  curl http://127.0.0.1:5000/health

If Flask is not installed and internet is disconnected, stop retrying pip. Ask the lab instructor for the approved offline wheel/cache. The source code itself is ready, but Flask cannot be installed from the internet while offline.

LOCAL GIT BRANCHES
From PowerShell in the extracted pack folder:
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  .\setup-local-git.ps1

This creates three branches. It requires Git and will make commits locally without internet.

GITHUB (only when internet is available and the empty GitHub repo is created):
  git remote add origin https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY.git
  git push -u origin v1
  git push -u origin v2
  git push -u origin v3

DOCKER (inside the version folder, replace username):
  docker build -t YOUR_DOCKERHUB_USERNAME/hospital-system:v1 .
  docker run --rm -p 5001:5000 YOUR_DOCKERHUB_USERNAME/hospital-system:v1
  docker login
  docker push YOUR_DOCKERHUB_USERNAME/hospital-system:v1
For v2/v3 use tags v2/v3 and host ports 5002/5003.

KUBERNETES (from a version folder after replacing username):
  kubectl apply -f k8s-deployment.yaml
  kubectl get deployments
  kubectl get services
  kubectl get pods

NodePorts: v1=30081, v2=30082, v3=30083. The exact browser URL depends on the lab's Kubernetes setup (localhost vs node IP).

JENKINS
- Create a Pipeline job and choose “Pipeline script from SCM”, Git, your repo URL, and the branch v1/v2/v3. The Jenkinsfile uses `checkout scm` and Windows `bat` steps.
- Replace Docker Hub username in Jenkinsfile before running.
- The supplied Jenkinsfile builds the Docker image; Docker Hub push is manual in the commands above. If Sir explicitly requires pipeline push, add a credentials-backed push stage according to the lab's credential setup.

kubectl apply -f v1/service.yaml
kubectl apply -f v2/service.yaml
kubectl apply -f v3/service.yaml

kubectl get services
kubectl get deployments
kubectl get pods