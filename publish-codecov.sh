docker-compose -f $1 build
docker-compose -f $1 up -d
docker-compose -f $1 exec api bash -c "sh run-tests.sh"
docker-compose -f $1 rm -f -s
cd api/api_gateway && codecov -t ${CODECOV_TOKEN}