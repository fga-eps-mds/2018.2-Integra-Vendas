default:
	docker build . -t docker-django:api-gateway
	docker run --rm -p 5000:5000 -v `pwd`:"/app" -w "/app" -it docker-django:api-gateway bash