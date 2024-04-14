pipeline {
    agent any

    environment {
        // Define Docker image name
        DOCKER_IMAGE = 'snake-game:latest'
        DOCKER_REGISTRY = 'smitwaman/snake-game'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from Git repository
                checkout scm
            }
        }

        stage('SonarQube Scan') {
            steps {
                withSonarQubeEnv('sonar') {
                    // Run SonarScanner
                    sh '''
                         sonar \
                        -Dsonar.projectKey=snake-game \
                        -Dsonar.sources=src \
                        -Dsonar.host.url=http://localhost:9000 \
                        -Dsonar.login=4801cac1ac5f143ceeed233425c210e699952339
                    '''
                }
            }
        }
    }
}
