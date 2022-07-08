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
                DOCKER_UNAME = credentials('docker_username')
                DOCKER_PWORD = credentials('docker_password')            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_UNAME -p $DOCKER_PWORD"
                sh "docker-compose push"
            }
        }
    }
}