#!/bin/sh
set -e

docker-compose -f $1 build
docker-compose -f $1 up -d
echo "Running Integration Tests"
docker exec api-gateway bash -c "bash ./check-services.sh && sh run-tests.sh"
docker-compose -f $1 down
docker-compose -f $1 rm -f -s