👉 In this step we are going to configure in detailed steps.

1. Prometheus server
2. Node exporter
3. Grafana server

**1. Prometheus server**

To create a system user or system account for Prometheus, run the following command:
```
sudo useradd \
    --system \
    --no-create-home \
    --shell /bin/falso prometheus
```
+
— system — Will create a system account.
— no-create-home — We don’t need a home directory for Prometheus or any other system accounts in our case.
— shell /bin/false — It prevents logging in as a Prometheus user.
Prometheus — Will create a Prometheus user and a group with the same name.

Let’s check the latest version of Prometheus from the download page.

+

You can download the latest version or the LTS (Long Term Support) version.

You can also use the curl or wget command to download Prometheus.

```
To avoid permission issues, you need to set the correct ownership for the /etc/prometheus/ and data directory.

$ sudo chown -R prometheus:prometheus /etc/prometheus/ /data/://github.com/prometheus/prometheus/releases/download/v2.47.1/prometheus-2.47.1.linux-amd64.tar.gz
```

+

```
tar -xvf prometheus-2.47.1.linux-amd64.tar.gz

```

+

Usually, you would have a disk mounted to the data directory. For this tutorial, I will simply create a /data directory. Also, you need a folder for Prometheus configuration files.

```
sudo mkdir -p /data /etc/prometheus

```

We’ll change to the Prometheus directory and move some in there.

```
 cd prometheus-2.47.1.linux-amd64/
```

+

Let’s move the Prometheus binary and the promtool to the /usr/local/bin/ directory. The promtool is a command-line utility that provides various tools for checking Prometheus configuration files and data, such as the rule file, alert, time series data inspection, etc.

```
sudo mv prometheus promtool /usr/local/bin/
```

+

Let’s move the console libraries to the Prometheus configuration directory. Console templates allow for the creation of arbitrary consoles using the Go template language. You don’t need to worry about it if you’re just getting started.

```
sudo mv consoles/ console_libraries/ /etc/prometheus/

```

+

Lastly, let’s move the example of the main Prometheus configuration file.

```
sudo mv prometheus.yml /etc/prometheus/prometheus.yml
```

+
