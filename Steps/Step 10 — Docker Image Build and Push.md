## Step 10 — Docker Image Build and Push
We need to install the Docker tool in our system, Goto Dashboard → Manage Plugins → Available plugins → Search for Docker and install these plugins

Docker

Docker Commons

Docker Pipeline

Docker API

docker-build-step


With Docker plugins installed, navigate to Jenkins Tools to configure Docker. Put docker under Name and select latest under Docker version, click Apply and Save.


Let’s add the DockerHub credentials to the Jenkins Credentials, which falls under the ‘Stores scoped to Jenkins’ Global. Type in your username, password and a name for the ID and Description. I used docker both ID and Description. Click Create.


DockerHub credential created and save under Global credentials (unrestricted).


Let’s add the following pipeline script to our Jenkins pipeline.
```
stage("Docker Build & Push"){
            steps{
                script{
                   withDockerRegistry(credentialsId: 'docker', toolName: 'docker'){   
                       sh "docker build --build-arg TMDB_V3_API_KEY=Aj7ay86fe14eca3e76869b92 -t netflix ."
                       sh "docker tag netflix cloudezigns/netflix:latest "
                       sh "docker push cloudezigns/netflix:latest "
                    }
                }
            }
        }
        stage("TRIVY"){
            steps{
                sh "trivy image cloudezigns/netflix:latest > trivyimage.txt" 
            }
        }
```
Below is the output from Jenkins pipeline.


Let’s log into the DockerHub and see if the Netflix image is pushed to the repositories.


With the Netflix image pushed to DockerHub, let’s add the following stage to our Jenkins pipeline and then run via a new browser to see if it is running.
```
stage('Deploy to container'){
            steps{
                sh 'docker run -d --name netflix -p 8081:80 sevenajay/netflix:latest'
            }
        }
```
Viola! The Docker container is running as expected.


Netflix Movies
