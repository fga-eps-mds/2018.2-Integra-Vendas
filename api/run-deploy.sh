# PROJECT_NAME
# CONTAINER_NAME
# PREFIX
# IMAGE
# namespace as argument of script --> production or staging

namespace=$1

version=`cat VERSION`
echo "version: $version"

if [ -z "$version" ]; then
    echo 'version variable is not set'
    exit 1
fi

if [ -z "$1" ]; then
    echo 'deployment envionment not setted'
    exit 1
fi

if [ $1 = "production" ]; then
    prefix_version='stable-'
    category='latest-stable'
else
    prefix_version='dev-'
    category='latest'
fi

image_versioned=${PREFIX}/${IMAGE}:${prefix_version}${version}

kubectl set image deployment/$PROJECT_NAME $CONTAINER_NAME=$image_versioned -n $namespace
kubectl rollout status deployment/$PROJECT_NAME -n $namespace