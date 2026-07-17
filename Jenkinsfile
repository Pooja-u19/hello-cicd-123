pipeline {
    agent any
    environment {
        IMAGE = "hello-cicd:${BUILD_NUMBER}"
        APP_NAME = "hello-cicd-app"
    }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Build') {
            steps { sh 'docker build -t $IMAGE .' }
        }
        stage('Test') {
            steps { sh 'docker run --rm $IMAGE python -m pytest -v' }
        }
        stage('Deploy') {
            steps {
                sh 'docker rm -f $APP_NAME || true'
                sh 'docker run -d --name $APP_NAME -p 8081:5000 $IMAGE'
            }
        }
    }
    post {
        success { echo 'Pipeline succeeded — app deployed on port 8081.' }
        failure { echo 'Pipeline failed — check the stage logs above.' }
    }
}
