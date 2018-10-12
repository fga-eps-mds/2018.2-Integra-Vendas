default:
	docker-compose build
	docker-compose up

run:
	echo NEED_UPDATE

enter:
	docker-compose exec web bash

test:
	docker-compose exec web bash -c "cd api_gateway && python manage.py test"

production:
	docker-compose -f docker-compose-production.yml up