docker-compose -f $1 build
docker-compose -f $1 up -d
docker exec api-gateway -e CODECOV_TOKEN=${CODECOV_TOKEN} bash -c "sh run-tests.sh && cd api_gateway && codecov -t ${CODECOV_TOKEN}"
docker-compose -f $1 rm -f -s