## Step 5 — Install the Prometheus Plugin and Integrate it with the Prometheus server

Goto Manage Jenkins → Plugins → Available Plugins


Jenkins Plugins

Search for Prometheus and install it


Let’s go Jenkins System to configure Prometheus.


Nothing to change here. Click Apply and Save the configuration.

Let’s go to the Prometheus server and create a job_name using static_configs for the static target.
```
$ sudo nano /etc/prometheus/prometheus.yml
```
Make sure the Jenkins static target configuration is valid before you save and exit the Prometheus configuration file.


Next, let’s check the promtool to verify whether the configuration was SUCCESS or not
```
$ promtool check config /etc/prometheus/prometheus.yml
```
The promtool check was a SUCCESS.


Let’s use the POST request to reload the config file.
```
$ curl -X POST http://localhost:9090/-/reload
```
Now, let’s check our targets on the Prometheus server by using the public IP address along with port number 9090.
```
$ http://<ip>:9090/targets
```
You can see that Jenkins is included in the Prometheus Targets.


Prometheus Targets
Let’s add a dashboard for a better view in Grafana.

Click On Dashboard → + symbol → Import Dashboard


Use Id 9964 and click on load



Below is the Detailed overview from Jenkins.


Grafana Dashboard
