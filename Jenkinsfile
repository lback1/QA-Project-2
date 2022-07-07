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
                DOCKER_UNAME = docker-hub-credentials('docker_uname')
                DOCKER_PWORD = docker-hub-credentials('docker_pword')
            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_UNAME -p $DOCKER_PWORD"
                sh "docker-compose push"
            }
        }
        stage('Deploy') {
            steps {
                //
            }
        }
    }
}