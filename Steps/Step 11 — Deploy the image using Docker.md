## Step 11 — Kuberenetes Setup
Connect your machines to Putty or Mobaxtreme

We’ll install two Ubuntu 20.04 instances one for k8s master and the other one for worker. Also, we’ll install Kubectl on our Jenkins machine for the Kubernetes.

Configure Two Ubuntu 20.04 instances
First, we’ll configure two Ubuntu 20.04 instances for Kubernetes (one for master and the other for worker).



Install Kubectl on Jenkins
Second, let’s install kubectl on the Jenkins server using the command below:
```
$ sudo apt update
$ sudo apt install curl
$ curl -LO https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl
$ sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
$ kubectl version - client
```
** Part 1 —Master Node — **
Let’s work on the master node by changing its name with the below command:

```
$ sudo hostnamectl set-hostname K8s-Master
— Worker Node —
$ sudo hostnamectl set-hostname K8s-Worker
```

** Part 2— Both Master & Node — **
```
$ sudo apt-get update
$ sudo apt-get install -y docker.io
$ sudo usermod -aG docker ubuntu
$ newgrp docker
$ sudo chmod 777 /var/run/docker.sock
$ sudo curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
$ sudo tee /etc/apt/sources.list.d/kubernetes.list <<EOF
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF
$ sudo apt-get update
$ sudo apt-get install -y kubelet kubeadm kubectl
$ sudo snap install kube-apiserver
```

** Part 3— Master — **
```
$ sudo kubeadm init --pod-network-cidr=10.244.0.0/16
  # in case your in root exit from it and run below commands
$ mkdir -p $HOME/.kube
$ sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
$ sudo chown $(id -u):$(id -g) $HOME/.kube/config
$ kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```

**— Worker Node — **
```
sudo kubeadm join <master-node-ip>:<master-node-port> — token <token> — discovery-token-ca-cert-hash <hash>
```
This is my discovery token for the worker node. It’s generated after you run the ‘sudo kubeadm init — pod-network-cidr=10.244.0.0/16’ on the Kubernetes master node.
```
kubeadm join 10.0.1.91:6443 — token w4j7yg.9mr663kzo0rb4efh \
 — discovery-token-ca-cert-hash sha256:69b3cda3cb9d019ef71457f05054aee74eeacce58e36ea39622e88f014ca8db0
The below configuration is for the Kubernetes Master Node. First, we access the Kubernetes master node using ssh -i jenkins-keys.pem ubuntu@18.220.20.49, change the name and reboot. Second, we update the master node and install the docker package and configure it. Next, we install other configuration packages and ensure everything is working properly.
```



The below configuration is for the Kubernetes Worker Node. First, we access the Kubernetes worker node using ssh -i jenkins-keys.pem ubuntu@52.15.165.0, change the name and reboot.




Let’s navigate to the worker node to execute the ‘kubeadm join’ command to join the nodes.
```
kubeadm join 10.0.42.152:6443 — token faezg3.5vufgwogdbyqe2er \
 — discovery-token-ca-cert-hash sha256:4cbf4c65f983728acdd2bb9417cdd49c6d3890c99166f230b8bb117834a3e454
```
With the ‘kubeadm join’ command administered, change to ‘/.kube’ directory on the master node and open the config file: ‘cat config’. Copy the ‘config file’ and save it as ‘secret-file.txt’ in a safe place. This file will be used for Kubernetes credentials on Jenkins.


Config File
Now, let’s install the four Kubernetes plugins on Jenkins.


Kubernetes Plugins
Let’s configure the credentials for Kubernetes on Jenkins. Click Add Credentials.


Global Credentials
Select the ‘secrefile.txt’ file under File/Choose File.


ID and Description can have the same name. In my case, I named it ‘’k8s and click Create.


Kubernetes credential is created as seen in the image below.


Install Node_exporter on both master and worker
Next, we’ll append Node_Exporter to both the Master and Worker nodes to monitor the metrics. First, will create a system user for the node-exporter by running the below command and use the ‘wget’ command to download it the binary form Node_Exporter home page:
```
sudo useradd \
  --system \ 
  --no-create-home \
  --shell /bin/false node_exporter
```
```
wget https://github.com/prometheus/node_exporter/releases/download/v1.6.1/node_exporter-1.6.1.linux-amd64.tar.gz
```


We’ll use the following command to extract the download:
```
tar -xvf node_exporter-1.6.1.linux-amd64.tar.gz
```
Next, we move the binary files here: /usr/local/bin. Used the command below.
```
sudo mv \
 node_exporter-1.6.1.linux-amd64/node_exporter \
 /usr/local/bin/
```
Now, let’s clean up and delete the node_exporter archive and folder.
```
rm -rf node_exporter*
```
Verify that you can run the binary.
```
node_exporter — version
```
Node Exporter has a lot of plugins that we can enable. Run Node Exporter help to get all the options.
```
node_exporter --help
```
— collector.logind We’re going to enable the login controller, just for the demo.

Next, create a similar systemd unit file.
```
sudo nano /etc/systemd/system/node_exporter.servicenode_exporter.service

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

To automatically start the Node Exporter after reboot, enable the service.
```
sudo systemctl enable node_exporter
```
Then start the Node Exporter.
```
sudo systemctl start node_exporter
```
Let’s check the status of Node Exporter with the following command:
```
sudo systemctl status node_exporter
```
If you come across any issues, check logs with journalctl.
```
journalctl -u node_exporter -f — no-pager
```
At this point, we have only a single target in our Prometheus. There are many different service discovery mechanisms built into Prometheus. For example, Prometheus can dynamically discover targets in AWS, GCP, and other clouds based on the labels. In the following tutorials, I’ll give you a few examples of deploying Prometheus in a cloud-specific environment. For this tutorial, let’s keep it simple and keep adding static targets. Also, I have a lesson on how to deploy and manage Prometheus in the Kubernetes cluster.

To create a static target, you need to add job_name with static_configs. Go to Prometheus server

First, install Prometheus using the following command:
```
wget https://github.com/prometheus/prometheus/releases/download/v2.30.0/prometheus-2.30.0.linux-amd64.tar.gz
```
Extract Prometheus using this command:
```
tar xvfz prometheus-2.30.0.linux-amd64.tar.gz
```
Move Prometheus to /usr/local/prometheus
```
sudo mv prometheus-2.30.0.linux-amd64 /usr/local/prometheus
```
Let’s open Prometheus configuration yml file.
```
sudo nano /etc/prometheus/prometheus.yml
```

Since we enabled lifecycle management via API calls, we can reload the Prometheus config without restarting the service and causing downtime.

Before, restarting check if the config is valid.
```
promtool check config /etc/prometheus/prometheus.yml
```
Then, you can use a POST request to reload the config. Make sure you execute the command below on the Prometheus server. Do not execute it on the Master node!
```
curl -X POST http://localhost:9090/-/reload
```
Check the targets section on the Prometheus server by executing this:
```
<prometheus_ip_server_address>:9090
```
The Master-node and Worker-node are exposed on the Prometheus server targets as indicated in the below image.


Prometheus Targets Exposed Node_Exporter on The Master-Node & Worker-Node
Now is the time to deploy the Kubernetes cluster on the Jenkins script pipeline.
```
stage('Deploy to kubernets'){
            steps{
                script{
                    dir('Kubernetes') {
                        withKubeConfig(caCertificate: '', clusterName: '', contextName: '', credentialsId: 'k8s', namespace: '', restrictKubeConfigAccess: false, serverUrl: '') {
                                sh 'kubectl apply -f deployment.yml'
                                sh 'kubectl apply -f service.yml'
                        }   
                    }
                }
            }
        }
```

The Jenkin pipeline view stage.


In the Kubernetes cluster(master) give this command
```
kubectl get all 
kubectl get svc #use anyone
```
