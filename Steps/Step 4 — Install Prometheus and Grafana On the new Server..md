👉 In this step we are going to configure in detailed steps.

1. Prometheus server
2. Node exporter
3. Grafana server

Step 4: Install Prometheus and Grafana On the new Server
Let’s create a dedicated Linux user called ‘system’ user for Prometheus and another user called ‘system’ account for Grafana. Having individual users for each service serves two main purposes:

It is a security measure to reduce the impact in case of an incident with the service.
It simplifies administration as it becomes easier to track down what resources belong to which service.
To create a system user or system account for Prometheus, run the following command:
```
$ sudo useradd \
    --system \
    --no-create-home \
    --shell /bin/falso prometheus
```

— system — Will create a system account.

— no-create-home — We don’t need a home directory for Prometheus or any other system accounts in our case.

— shell /bin/false — It prevents logging in as a Prometheus user.

Prometheus — Will create a Prometheus user and a group with the same name.

Let’s check the latest version of Prometheus from the download page.


Prometheus Download Page
You can download the latest version or the LTS (Long Term Support) version.

You can also use the curl or wget command to download Prometheus.

```
$ wget https://github.com/prometheus/prometheus/releases/download/v2.47.1/prometheus-2.47.1.linux-amd64.tar.gz
```

Prometheus -2.47.1 Linux-amd64 Downloaded

Next, we need to extract all the Prometheus files from the archive. We’ll do that using the following command:
```
$ tar -xvf prometheus-2.47.1.linux-amd64.tar.gz
```

Extract Prometheus From Archive Using The Command Above

Usually, you would have a disk mounted to the data directory. For this tutorial, I will simply create a /data directory. Also, you need a folder for Prometheus configuration files.
```
$ sudo mkdir -p /data /etc/prometheus

```

We’ll change to the Prometheus directory and move some in there.

```
$ cd prometheus-2.47.1.linux-amd64/
```

Let’s move the Prometheus binary and the promtool to the /usr/local/bin/ directory. The promtool is a command-line utility that provides various tools for checking Prometheus configuration files and data, such as the rule file, alert, time series data inspection, etc.

```
$ sudo mv prometheus promtool /usr/local/bin/
```

Let’s move the console libraries to the Prometheus configuration directory. Console templates allow for the creation of arbitrary consoles using the Go template language. You don’t need to worry about it if you’re just getting started.

```
$ sudo mv consoles/ console_libraries/ /etc/prometheus/
```

Lastly, let’s move the example of the main Prometheus configuration file.

```
$ sudo mv prometheus.yml /etc/prometheus/prometheus.yml
```

To avoid permission issues, you need to set the correct ownership for the /etc/prometheus/ and data directory.

```
$ sudo chown -R prometheus:prometheus /etc/prometheus/ /data/
```

You can delete the archive and a Prometheus folder when you are done.

```
$ cd rm -rf prometheus-2.47.1.linux-amd64.tar.gz
```

Let’s verify that we can execute the Prometheus binary by running the following command:

```
$ prometheus — version
```

For help, run Prometheus Help.
```
$ prometheus --help
```

We’ll use some of these options in the service definition.

We’re going to use Systemd, which is a system and service manager for Linux operating systems. For that, we need to create a Systemd unit configuration file.
```
$ sudo nano /etc/systemd/system/prometheus.service

Prometheus.service
[Unit]
Description=Prometheus
Wants=network-online.target
After=network-online.target

StartLimitIntervalSec=500
StartLimitBurst=5

[Service]
User=prometheus
Group=prometheus
Type=simple
Restart=on-failure
RestartSec=5s
ExecStart=/usr/local/bin/prometheus \
  --config.file=/etc/prometheus/prometheus.yml \
  --storage.tsdb.path=/data \
  --web.console.templates=/etc/prometheus/consoles \
  --web.console.libraries=/etc/prometheus/console_libraries \
  --web.listen-address=0.0.0.0:9090 \
  --web.enable-lifecycle

[Install]
WantedBy=multi-user.target

A few of the most important options related to Systemd and Prometheus. Restart — Configures whether the service shall be restarted when the service process exits, is killed, or a timeout is reached.
RestartSec — Configures the time to sleep before restarting a service.
User and Group — Are Linux user and a group to start a Prometheus process.
— config.file=/etc/prometheus/prometheus.yml — Path to the main Prometheus configuration file.
— storage.tsdb.path=/data — Location to store Prometheus data.
— web.listen-address=0.0.0.0:9090 — Configure to listen on all network interfaces. In some situations, you may have a proxy such as nginx to redirect requests to Prometheus. In that case, you would configure Prometheus to listen only on localhost.
— web.enable-lifecycle — Allows you to manage Prometheus, for example, to reload configuration without restarting the service.

To automatically start the Prometheus after reboot, run enable.
```
```
$ sudo systemctl enable prometheus
```
Now that the Prometheus is enable, start it by executing the following command:
```
$ sudo systemctl start prometheus
```
Run the following command to check the status of the Prometheus.
```
$ sudo systemctl status prometheus
```
If you encounter any issues with Prometheus or are unable to start it, the easiest way to find the problem is to use the journalctl command and search for errors.
```
$ journalctl -u prometheus -f --no-pager

```
Now we can try to access it via the browser. I’m going to be using the public IP address of the Ubuntu instance along wth port number 9090.
```
$ <public-ip:9090>
```
If you go to targets, you should see only one — Prometheus target. It scrapes itself every 15 seconds by default.



## Install Node Exporter on Ubuntu 22.04
Next, we’re going to set up and configure Node Exporter to collect Linux system metrics like CPU load and disk I/O. Node Exporter will expose these as Prometheus-style metrics. Since the installation process is very similar, I’m not going to cover as deep as Prometheus.

First, let’s create a system user for Node Exporter by running the following command:
```
sudo useradd \
  --system \
  --no-create-home \
  --shell /bin/false node_exporter
```
You can download Node Exporter from here or use the’ wget’ command to download the binary.
```
wget https://github.com/prometheus/node_exporter/releases/download/v1.6.1/node_exporter-1.6.1.linux-amd64.tar.gz
```
Extract the node exporter from the archive.
```
$ tar -xvf node_exporter-1.6.1.linux-amd64.tar.gz
```
Move binary to the /usr/local/bin.
```
$ sudo mv \
  node_exporter-1.6.1.linux-amd64/node_exporter \
  /usr/local/bin/
```
Let’s clean up and delete the node_exporter archive and a folder.
```
$ rm -rf node_exporter*
```
Let’s verify that we can run the binary.
```
$ node_exporter — version
```
Node Exporter has a lot of plugins that be can enabled. You can run the Node Exporter help to get all the options.
```
$ node_exporter --help
```
Let’s enable the login controller just for the demo ‘— collector.logind’.

Next, create a similar systemd unit file for node_exporter.
```
$ sudo nano /etc/systemd/system/node_exporter.service
node_exporter.service
[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

StartLimitIntervalSec=500
StartLimitBurst=5

[Service]
User=node_exporter
Group=node_exporter
Type=simple
Restart=on-failure
RestartSec=5s
ExecStart=/usr/local/bin/node_exporter \
    --collector.logind

[Install]
WantedBy=multi-user.target
```
Replace Prometheus user and group to node_exporter, and update the ExecStart command.

To automatically start the Node Exporter after reboot, enable the service with the following command:
```
$ sudo systemctl enable node_exporter
```
Start the Node Exporter with this command:
```
$ sudo systemctl start node_exporter
```
Check the status of Node Exporter with the following command:
```
$ sudo systemctl status node_exporter
```
If you have any issues, check logs with journalctl
```
$ journalctl -u node_exporter -f — no-pager

```
At this point, we have only a single target in our Prometheus. There are many different service discovery mechanisms built into Prometheus. For example, Prometheus can dynamically discover targets in AWS, GCP, and other clouds based on the labels. In the following tutorials, I’ll give you a few examples of deploying Prometheus in a cloud-specific environment. For this tutorial, let’s keep it simple and keep adding static targets. Also, I have a lesson on how to deploy and manage Prometheus in the Kubernetes cluster.

To create a static target, you need to add job_name with static_configs.
```
$ sudo nano /etc/prometheus/prometheus.yml
prometheus.yml
- job_name: node_export
  static_configs:
  - targets: [“localhost:9100”]
```
By default, Node Exporter will be exposed on port 9100.

Since we enabled lifecycle management via API calls, we can reload the Prometheus config without restarting the service and causing downtime.

Before, restarting check if the config is valid.
```
$ promtool check config /etc/prometheus/prometheus.yml
```
Then, you can use a POST request to reload the config.
```
$ curl -X POST http://localhost:9090/-/reload
```
Examine the targets section in Prometheus, utilizing the public IP address of the Ubuntu instance along with port number 9090.
```
$ http://<ip>:9090/targets
```


## Install Grafana on Ubuntu 22.04
Grafana is a powerful tool for visualizing metrics, and it supports various data sources. One such supported source is Prometheus.

Let’s ensure that all the necessary dependencies are installed.
```
$ sudo apt-get install -y apt-transport-https software-properties-common
```
Let’s add the GPG keys. The GNU Privacy Guard (GPG) or Pretty Good Privacy (PGP) keys provide a way to secure communication and ensure the integrity and authenticity of digital information.
```
$ wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
```
Let’s append the repository to the stable version of software releases of Grafana.
```
echo “deb https://packages.grafana.com/oss/deb stable main” | sudo tee -a /etc/apt/sources.list.d/grafana.list
```
Update and install Grafana after adding the repository to the stable releases.
```
$ sudo apt-get update
$ sudo apt-get -y install grafana
```
Let’s enable, start, and check the status of the Grafana server.
```
$ sudo systemctl enable grafana-server
$ sudo systemctl start grafana-server
$ sudo systemctl status grafana-server
```
We’ll use the public IP address of our Ubuntu instance along with the port number 3000 to examine the Grafana server. The default username and password are both ‘admin’.
```
$ http://<public_ip>:3000
$ username admin
$ password admin
```
Grafana Server
You’ll be prompted to change your password when you login the first time.


Log in Grafana Server

To see any metrics, you need to add data source.


Click ‘Add your first data source’ and select Prometheus.


Enter localhost:9090 for the URL.
```
$ http://localhost:9090
```
Scroll down and click Save and Test.



For a better view, let’s add a Dashboard. Select Import Dashboard from the dropdown menu.


Import Dashboard
Type in this code 1860 and click on load


Select the Datasource and click on Import

The below output is what you will see.


                                                                Grafana Dashboard
