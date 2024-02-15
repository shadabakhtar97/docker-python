pipeline {

  environment {
    frontendDockerImageName = "sample-frontend:v1"
    backendDockerImageName = "sample-backend:v1"
    dockerImage = ""
    registryCredential = 'dockerhublogin'
  }

  agent any

  stages {

    stage('Checkout Source') {
      steps {
        git 'https://github.com/shadabakhtar97/docker-python.git'
      }
    }

    stage('Build Frontend Image') {
      steps {
        script {
          dockerImage = docker.build frontendDockerImageName
        }
      }
    }

    stage('Push Frontend Image') {
      steps {
        script {
          docker.withRegistry('https://registry.hub.docker.com', registryCredential) {
            dockerImage.push("${frontendDockerImageName}")
          }
        }
      }
    }

    stage('Build Backend Image') {
      steps {
        script {
          dockerImage = docker.build backendDockerImageName
        }
      }
    }

    stage('Push Backend Image') {
      steps {
        script {
          docker.withRegistry('https://registry.hub.docker.com', registryCredential) {
            dockerImage.push("${backendDockerImageName}")
          }
        }
      }
    }

  }

}



