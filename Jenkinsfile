pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = 'abc'
        DOCKERHUB_USER = 'dockerhubuser'
    }

    stages {
        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Build Images') {
            steps {
                sh '''
                docker build -t $DOCKERHUB_USER/infraback:latest backend
                docker build -t $DOCKERHUB_USER/infraweb:latest webui
                '''
            }
        }

        stage('Login & Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: DOCKERHUB_CREDENTIALS,
                    usernameVariable: 'U',
                    passwordVariable: 'P'
                )]) {
                    sh '''
                    echo $P | docker login -u $U --password-stdin
                    docker push $DOCKERHUB_USER/infraback:latest
                    docker push $DOCKERHUB_USER/infraweb:latest
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                kubectl apply -n app -f k8s/backend.yaml
                kubectl apply -n app -f k8s/webui.yaml
                '''
            }
        }
    }
}
