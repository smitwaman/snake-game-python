## Step 7 — Install Plugins like JDK, Sonarqube Scanner, NodeJs, OWASP Dependency Check

7B — Configure Java and Nodejs in Global Tool Configuration
Let’s configure JDK17 and NodeJs16 by going to Manage Jenkins → Tools.



Click on Apply and Save.

Next, let’s create our pipeline and insert the block below.
```

post {
     always {
        emailext attachLog: true,
            subject: "'${currentBuild.result}'",
            body: "Project: ${env.JOB_NAME}<br/>" +
                "Build Number: ${env.BUILD_NUMBER}<br/>" +
                "URL: ${env.BUILD_URL}<br/>",
            to: 'postbox.aj99@gmail.com',  #change Your mail
            attachmentsPattern: 'trivyfs.txt,trivyimage.txt'
        }
    }

```

The Hello World template gives you the default configuration of the pipeline. Use it!
