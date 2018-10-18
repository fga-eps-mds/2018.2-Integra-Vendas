default:
	cd api && make

run:
	cd api && make run

integration-tests:
	docker-compose -f ${file} build
	docker-compose -f ${file} up -d
	docker exec api-gateway bash -c "sh run-integration-tests.sh"
	docker-compose -f ${file} rm -f -s

staging-integration-tests:
	make integration-tests file=dc-integration-test.staging.yml

production-integration-tests:
	make integration-tests file=dc-integration-test.production.yml