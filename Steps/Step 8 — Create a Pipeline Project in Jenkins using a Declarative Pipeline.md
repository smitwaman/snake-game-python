## Step 8 — Configure Sonar Server in Manage Jenkins
Let’s configure the SonarQube server in Manage Jenkins | Tools.





Now, let’s activate SonarQube via our Ubuntu instance terminal by using this command:
```
$ docker run -d --name sonar -p 9000:9000 sonarqube:lts-community
```
Next, let’s use the public IP address of our Ubuntu instance along with port number 9000 and open a new browser to access the SonarQube server. Type admin twice for username and password to update password and login.










In the SonarQube server Dashboard, click Configuration, Webhooks, and create Webhooks for Jenkins and Prometheus.


Create the Webhook by typing the name and URL as shown below.
```
http://<jenkins-ip>:8080/sonarqube-webhook
```

Let’s navigate to our Jenkins pipeline and start the script of our pipeline.
```
pipeline {
    agent any
    
    tools {
        jdk 'jdk17'
        nodejs 'node16'
    }
    
    environment {
        
        SCANNER_HOME= tool 'sonar-scanner'
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
        
        stage('Checkout from GITHUB') {
            steps {
                git branch: 'main', url: 'https://github.com/cloudezigns/Netflix-clone.git'
            }
        }
        
        stage('SonarQube Scan Analysis') {
            steps {
                withSonarQubeEnv('sonar-server') {
                    sh ''' $SCANNER_HOME/bin/sonar-scanner -Dsonar.projectName=Netflix \
                    -Dsonar.projectKey=Netflix '''
                }
           }
        }
        
        stage('Quality Gate') {
            steps {
                waitForQualityGate abortPipeline: false, credentialsId: 'Sonar-token'
            }
        }
        
        stage('Install NodeJs Dependencies') {
            steps {
                sh 'npm install'
            }
        }
    }
    
     post {
     always {
        emailext attachLog: true,
            subject: "'${currentBuild.result}'",
            body: "Project: ${env.JOB_NAME}<br/>" +
                "Build Number: ${env.BUILD_NUMBER}<br/>" +
                "URL: ${env.BUILD_URL}<br/>",
            to: 'postbox.aj99@gmail.com',
            attachmentsPattern: 'trivyfs.txt,trivyimage.txt'
        }
    }
}
```
Below is the output of our Stage View.


Stage View of Our Pipeline
Let’s navigate to our SonarQube server and click on ‘Projects’ to view the report. According to the report, 3.2k lines were scanned, revealing 18 code smells, all of which passed. It’s important to note that code smells are not bugs or errors; rather, they are patterns or structures in the code that might indicate issues. They are termed ‘smells’ because they serve as signs that something might be wrong with the code. In our case, we have received an ‘A’ grade, indicating that there is nothing wrong with our code.


