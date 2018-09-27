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

clean: clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

create-keys: ## creates a rsa key pair
	$(MAKE) compose-build
	docker-compose run web bash -c "python create_keys.py"
	$(MAKE) compose-down

compose-build:
	@docker-compose build

compose-down:
	@docker-compose down

type-check: ## check types with mypy
	$(MAKE) compose-build
	docker-compose run --rm web bash -c "mypy {{cookiecutter.app_name}} && rm -r .mypy_cache"
	$(MAKE) compose-down

lint: ## check style with flake8
	$(MAKE) compose-build
	docker-compose run --rm web bash -c "flake8"
	$(MAKE) compose-down

test: # run django tests
	$(MAKE) compose-build
	docker-compose run web bash -c "python wait_for_postgres.py && python manage.py test"
	$(MAKE) compose-down

start-dev: ## starts development server
	$(MAKE) compose-build
	docker-compose up
