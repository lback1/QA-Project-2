pipeline {
    agent any
    stages {
        stage('unit tests') {
            steps {
                sh "bash test.sh"
            }
        }
        stage('build and push images') {
             environment {
             
                docker-hub-credentials = credentials('docker_username')
                docker-hub-credentials = credentials('docker_password')

            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                sh "docker-compose push"
            }
        }
    }
}
