## Step 6 — Email Integration With Jenkins and Plugin Setup
Install Email Extension Plugin in Jenkins.


Next, go to your Gmail account and click on Profile and then Manage your Google Account.


Select Security from the left-hard of your Google Account. Click 2-Step Verification to create your App password.


Click on the dropdown arrow of the App passwords.


Type in Jenkins and click Create to create your app password.


An App password similar to the one below will pop up for you.


With the Email Extension plugin installed, navigate to the Jenkins System to configure it your Email Notification.



Manage Jenkins System
Click on Manage Jenkins → Credentials and add your mail username and generated password.





Google email notification credential is now added to Jenkins Global credentials (unrestricted).

On the Jenkins System, under the Extended E-mail notification section, let’s configure it as shown in the image below.


Click Apply and save.

Next, let’s navigate to Jenkins to install JDK, Sonarqube scanner, NodeJs OWASP Dependencies-Check, and configure our pipeline. Install all the plugins without restarting the Jenkins server.
