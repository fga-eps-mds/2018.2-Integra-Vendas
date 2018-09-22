default:
	docker build . -t docker-django:api-gateway
	docker run --rm -p 5000:5000 -v `pwd`:"/app" -w "/app" -it docker-django:api-gateway bash

run:
	docker build . -t docker-django:api-gateway
	docker run --rm -p 5000:5000 -v `pwd`:"/app" -w "/app" -d docker-django:api-gateway bash -c "sh run-django.sh"