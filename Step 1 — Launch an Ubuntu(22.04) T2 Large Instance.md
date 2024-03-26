Launch an Ubuntu (22.04) LTS t2.Large instance from the AWS Home Console under EC2. If you don’t have an active AWS account, you can create one by clicking on this link. The image below illustrates the configuration settings for the Ubuntu instance.

Copy the shell script below and paste it into the ‘User data’ section. Review the configuration settings, and then click on ‘Launch Instance. The shell script updates the Ubuntu instance and installs JDK Java (Temurin), Jenkins, Docker, Trivy, and Kubectl. Pretty cool, right? Lol!

You can also save the Bash script file as ‘netflix.sh’ using the nano editor (‘nano netflix.sh’). Paste the script, save it, and run it from your Ubuntu instance terminal. Don’t forget to execute the ‘chmod +x netflix.sh’ command in your terminal before running the script ‘./tools.sh'


![EC2 launch with tools.sh](https://github.com/smitwaman/devops-netflix-pipeline/blob/main/images%2Fnetflix-demo-images%2FEC2%2F17113764910746965517050830563332.jpg)

