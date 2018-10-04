#install kubectl
apt-get update && apt-get install -y apt-transport-https
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
touch /etc/apt/sources.list.d/kubernetes.list 
echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list
apt-get update
apt-get install -y kubectl

if [ -z "$KUBE_CONFIG" ]; then
    echo "KUBE_CONFIG variable not setted"
    exit 1
fi

mkdir $HOME/.kube
export KUBECONFIG=$KUBECONFIG:$HOME/.kube/config

#configure kubectl
echo $KUBE_CONFIG | base64 -d > $HOME/.kube/config
