pipeline {
    agent any

    environment {
        // Define environment variables
        DOCKER_IMAGE = 'snake-game:latest'
        DOCKER_REGISTRY = 'smitwaman/snake-game'
    }

    tools {
        // Define Python installation
        python 'Python3'
        // Define SonarScanner tool
        sonarqube 'SonarQubeScanner'
    }

    stages {
        stage('wsclean') {
            steps {
                // wsclean steps
                sh '''
                    # Add your wsclean commands here
                '''
            }
        }

        stage('Python venv build') {
            steps {
                // Create Python virtual environment and build
                sh '''
                    python3 -m venv myenv
                    source myenv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('SonarQube Scan') {
            steps {
                script {
                    // Run SonarScanner
                    sh '''
                        sonar-scanner \
                        -Dsonar.projectKey=snake-game \
                        -Dsonar.sources=src \
                        -Dsonar.host.url=http://localhost:9000 \
                        -Dsonar.login=4801cac1ac5f143ceeed233425c210e699952339 \
                        -Dsonar.analysis.mode=preview \
                        -Dsonar.dryRun=true
                    '''
                }
            }
        }

        stage('Docker Image Build and Push') {
            steps {
                script {
                    // Build Docker image
                    docker.build(DOCKER_IMAGE)

                    // Push Docker image to Docker registry
                    docker.withRegistry('https://${DOCKER_REGISTRY}', 'docker') {
                        docker.image(DOCKER_IMAGE).push()
                    }
                }
            }
        }
    }

    post {
        always {
            // Cleanup or post-build actions can be added here
        }
    }
}
