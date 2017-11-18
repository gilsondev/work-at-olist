.PHONY: setup local_setup run

setup:
	pip install -r requirements.txt

local_setup:
	pip install -r requirements-local.txt
	cp -Rvf local.env .env

run:
	@docker-compose up -d
	python work-at-olist/manage.py runserver