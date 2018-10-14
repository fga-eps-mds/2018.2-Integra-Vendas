set -e

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


if [ -z "$PREFIX" ]; then
    echo 'PREFIX variable is not set'
    echo "${PREFIX2} variable is not set"
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

# build
docker build -t $image_latest -f production.Dockerfile .

# login docker hub
docker login -u $DC_USER -p $DC_PASS

# push latest
echo "publishing latest: ${image_latest}"
docker push ${image_latest}

if [ $1 = "production" ]; then
    # tag it
    docker tag $image_latest $image_versioned

    # push versioned stable
    echo "publishing version: $${image_versioned}"
    docker push ${image_versioned}
fi

