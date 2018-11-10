default:
	cd api && make

run:
	cd api && make run

integration-tests:
	docker-compose -f ${file} build
	docker-compose -f ${file} up -d
	echo "Running Integration Tests"
	docker exec api-gateway bash -c "ls && bash ./check-services.sh && sh run-tests.sh"
	docker-compose -f ${file} down
	docker-compose -f ${file} rm -f -s

staging-integration-tests:
	sh remove-all-containers.sh || true
	make integration-tests file=dc-integration-test.staging.yml

production-integration-tests:
	sh remove-all-containers.sh || true
	make integration-tests file=dc-integration-test.production.yml

backend:
	sh remove-all-containers.sh || true
	docker-compose -f dc-backend-production.yml build
	docker-compose -f dc-backend-production.yml up 

build-staging:
	docker-compose -f dc-integration-test.staging.yml build

remove-staging-images:
	docker rmi integravendas/order-microservice:latest integravendas/product-microservice:latest integravendas/login-microservice:latest integravendas/notification-microservice:latest

run-staging-tests:
	sh remove-all-containers.sh || true
	make run-integration-tests file=dc-integration-test.staging.yml

run-integration-tests:
	docker-compose -f ${file} up -d
	echo "Running Integration Tests"
	docker exec api-gateway bash -c "bash ./check-services.sh && sh run-tests.sh"
	docker-compose -f ${file} down
	docker-compose -f ${file} rm -f -s

build-production:
	docker-compose -f dc-integration-test.production.yml build
