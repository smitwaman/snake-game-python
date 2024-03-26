## Step 9 — Install OWASP Dependency Check Plugins
Let’s navigate to the Jenkins Dashboard → Manage Jenkins → Plugins and search for → OWASP Dependency-Check.


Let’s install the OWASP Dependency-Check plugin and configure it in Jenkins Tools.



Click Apply and Save.

Next, we need to integrate the OWASP Dependency-Check script to our Jenkins pipeline to perform a continuous inspection of our source code along with Trivy which will perform vulnerability scans on our Docker and Kubernetes containerized images.
```
stage('OWASP FS SCAN') {
            steps {
                dependencyCheck additionalArguments: '--scan ./ --disableYarnAudit --disableNodeAudit', odcInstallation: 'DP-Check'
                dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
            }
        }
        stage('TRIVY FS SCAN') {
            steps {
                sh "trivy fs . > trivyfs.txt"
            }
        }
```
Below is the stage overview


