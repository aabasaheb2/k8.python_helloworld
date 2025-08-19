In this project, we will be doing the following.

1. Create a Hello World application in Python.
2. Create a Dockerfile for our Hello World application.
3. Create a Docker image for our application.
4. Deploy Docker image onto Kubernetes cluster.
5. Access our application via browser.

Create the cluster using the configuration file:
kind create cluster --config kind-config.yaml --name tws-kind-cluster

Verify the cluster:
kubectl get nodes
kubectl cluster-info

Use kubectl to interact with the cluster:
kubectl cluster-info

Apply all the manifest files present in the current directory.
kubectl apply -f .

Run this command to get all resources created in recreate-ns namespace.
kubectl get all -n ns_name

Forward the svc port to the EC2 instance port 3000
kubectl port-forward --address 0.0.0.0 svc/recreate-service 3000:3000 -n recreate-ns &     (add svc name)

Open the inbound rule for port 3000 in that EC2 Instance and check the application at URL:
http://<Your_Instance_Public_Ip>:3000

Open a new tab of terminal and connect your EC2 instance and run the watch command to monitor the deployment
watch kubectl get pods -n recreate-ns

Cleanup
Deleting Kind Cluster:

kind delete cluster --name dep-strg

Delete the KIND cluster:
kind delete cluster --name my-kind-cluster
