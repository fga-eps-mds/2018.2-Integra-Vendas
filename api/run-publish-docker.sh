set -e

if [ -z "$PREFIX" ]; then
    echo 'PREFIX variable is not set'
    exit 1
fi

if [ -z "$IMAGE" ]; then
    echo 'IMAGE variable is not set'
    exit 1
fi

if [ -z "$DC_USER" ]; then
    echo 'DC_USER variable is not set'
    exit 1
fi

if [ -z "$DC_PASS" ]; then
    echo 'DC_PASS variable is not set'
    exit 1
fi

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

image_latest=$PREFIX/$IMAGE:$category
image_versioned=${PREFIX}/${IMAGE}:${prefix_version}${version}

echo 'building images...'
echo "latest   \t-> ${image_latest}"
echo "versioned\t-> ${image_versioned}"

docker build -t $image_latest -f production.Dockerfile .

# tag it
docker tag $image_latest $image_versioned

# login docker hub
docker login -u $DC_USER -p $DC_PASS

# push it
echo "publishing latest: ${image_latest}"
docker push ${image_latest}
echo "publishing version: $${image_versioned}"
docker push ${image_versioned}
