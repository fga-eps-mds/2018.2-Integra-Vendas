default:
	docker network create api-backend || true
	docker-compose up

run:
	echo NEED_UPDATE

build:
	docker-compose build

enter:
	docker-compose exec web bash

test:
	docker-compose exec web bash -c "cd api_gateway && python manage.py test"

production:
	docker-compose -f docker-compose-production.yml build
	docker-compose -f docker-compose-production.yml up

down:
	docker-compose down

check-docker-production:
	make production &
	sleep 60
	bash check-container.sh
	docker-compose -f docker-compose-production.yml down

check-docker-dev:
	make &
	sleep 60
	bash check-container.sh
	make down