pipeline {
    agent any

    environment {
        GEMINI_KEY = credentials('gemini-api-key-id')
        APP_NAME = "house-predict"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build & Deploy') {
           
            steps {
                sh 'docker-compose up -d --build web-app'
            }
        }
    }
}