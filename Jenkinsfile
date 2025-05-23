pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'gym-membership-app'
        DOCKER_TAG = "${BUILD_NUMBER}"
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        PROJECT_DIR = '/var/lib/jenkins/app'
        EC2_HOST = '15.206.122.191'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} ."
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker run -d -p 5000:5000 --name test-container ${DOCKER_IMAGE}:${DOCKER_TAG}
                    sleep 10
                    curl -f http://localhost:5000 || exit 1
                    docker stop test-container
                    docker rm test-container
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh '''
                    echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin
                    docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKERHUB_CREDENTIALS_USR}/${DOCKER_IMAGE}:${DOCKER_TAG}
                    docker push ${DOCKERHUB_CREDENTIALS_USR}/${DOCKER_IMAGE}:${DOCKER_TAG}
                '''
            }
        }

        stage('Deploy to EC2') {
            steps {
                sshagent(['jenkins-ssh-key']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no ubuntu@${EC2_HOST} "docker pull ${DOCKERHUB_CREDENTIALS_USR}/${DOCKER_IMAGE}:${DOCKER_TAG}"
                        ssh -o StrictHostKeyChecking=no ubuntu@${EC2_HOST} "docker stop gym-app || true"
                        ssh -o StrictHostKeyChecking=no ubuntu@${EC2_HOST} "docker rm gym-app || true"
                        ssh -o StrictHostKeyChecking=no ubuntu@${EC2_HOST} "docker run -d -p 80:5000 --name gym-app ${DOCKERHUB_CREDENTIALS_USR}/${DOCKER_IMAGE}:${DOCKER_TAG}"
                    '''
                }
            }
        }
    }

    post {
        always {
            sh "docker logout"
            cleanWs()
        }
    }
}
