.PHONY: clean clean-test clean-pyc help
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

compose-build:
	@docker-compose build

compose-down:
	@docker-compose down

clean: clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-pyc: ## remove Python file artifacts
	$(MAKE) compose-build
	docker-compose run web bash -c " \
		find . -name '*.pyc' -exec rm -f {} + \
		find . -name '*.pyo' -exec rm -f {} + \
		find . -name '*~' -exec rm -f {} + \
		find . -name '__pycache__' -exec rm -fr {} + \
	"
	$(MAKE) compose-down

clean-test: ## remove test and coverage artifacts
	$(MAKE) compose-build
	docker-compose run web bash -c " \
		rm -fr .tox/ \
		rm -f .coverage \
		rm -fr htmlcov/ \
		rm -fr .pytest_cache \
		rm -fr .mypy_cache \
	"
	$(MAKE) compose-down

create-keys: ## creates a rsa key pair
	$(MAKE) compose-build
	docker-compose run web bash -c " \
		python create_keys.py \
	"
	$(MAKE) compose-down

type-check: ## check types with mypy
	$(MAKE) compose-build
	docker-compose run --rm web bash -c " \
		mypy {{cookiecutter.app_name}} && rm -r .mypy_cache \
	"
	$(MAKE) compose-down

lint: ## check style with flake8
	$(MAKE) compose-build
	docker-compose run --rm web bash -c " \
		flake8 \
	"
	$(MAKE) compose-down

test: # run django tests
	$(MAKE) compose-build
	docker-compose run web bash -c " \
		python wait_for_postgres.py &&  \
		python manage.py test && \
		rm -r .coverage \
	"
	$(MAKE) compose-down

start-dev: ## starts development server
	$(MAKE) compose-build
	docker-compose up

ci:
	docker-compose run \
		-e CODECOV_TOKEN=$CODECOV_TOKEN --rm web bash \
		-c " \
			flake8 . && \
			mypy {{cookiecutter.app_name}} && rm -r .mypy_cache \
			python wait_for_postgres.py && python manage.py test && codecov \
		"
