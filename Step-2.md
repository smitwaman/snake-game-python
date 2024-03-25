👉 Step by step access and configuration The Jenkins And SonarQube Servers

1. Jenkins server


With the Ubuntu instance launched and the script for Jenkins and SonarQube installed, let’s access the Jenkins and SonarQube server one at a time.

We’ll use the public IP address of the Ubuntu instance along with port 8080 and open a new browser to bring up the Jenkins server. The below image illustrates the series of steps for bringing up the Jenkins server. The Jenkins’ adminstrator password was copied, retrived from its log using the ‘sudo cat’ command, and pasted into the administrator password window to access the Jenkins server.
![](https://github.com/smitwaman/devops-netflix-pipeline/blob/main/images/netflix-demo-images/Jenkins/1711377059068648242202523632176.jpg)

Let’s create the ‘First Admin User’ by typing in our credentials in the image below. Click Save and Continue.

![](https://github.com/smitwaman/devops-netflix-pipeline/blob/main/images/netflix-demo-images/Jenkins/17113771038318238765125975349032.jpg)


User Credentials
Click on Save and Finish to complete the Jenkins Instance Configuration.

![](https://github.com/smitwaman/devops-netflix-pipeline/blob/main/images/netflix-demo-images/Jenkins/17113771130593098712904169130495.jpg)

Jenkins Configuration
Click on ‘Start using Jenkins’ to get the Jenkins welcome page.

![](https://github.com/smitwaman/devops-netflix-pipeline/blob/main/images/netflix-demo-images/Jenkins/17113771221194048793620322257795.jpg)

We’ll use the ‘Install suggested plugins’ to install our Jenkins plugins.


![](https://github.com/smitwaman/devops-netflix-pipeline/blob/main/images/netflix-demo-images/Jenkins/17113770786617482499777939673851.jpg)

Installing Jenkins Suggested Plugins
The suggested plugins are installed.

![](https://github.com/smitwaman/devops-netflix-pipeline/blob/main/images/netflix-demo-images/Jenkins/17113770940111473650138699486122.jpg)

                            Suggested Plugins





Welcome to Jenkins

![](https://github.com/smitwaman/devops-netflix-pipeline/blob/main/images/netflix-demo-images/Jenkins/17113771308797797277233676155905.jpg)



2. SonarQube server

With following command we will run our Sonarqube-Server.

```
docker run -d --name sonar -p 9000:9000 sonarqube:lts-community

```