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
                DOCKER_UNAME = credentials('DOCKER_UNAME')
                DOCKER_PWORD = credentials('DOCKER_PWORD')            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
                sh "docker-compose push"
            }
        }
    }
}