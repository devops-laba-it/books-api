.PHONY: venv
venv:
	test -f venv/bin/python || python3 -m venv venv
	venv/bin/pip install -q -U pip


.PHONY: deps
deps: venv
	venv/bin/python -m pip install -q -r requirements.txt


.PHONY: deps-dev
deps-dev: venv
	venv/bin/python -m pip install -q -r requirements-dev.txt

.PHONY: build
build: deps
	venv/bin/pip install -r requirements.txt --target python
	cp -r templates python
	cp lambda_function.py python
	(cd python; zip -r ../app ./)

.PHONY: run
run: deps-dev
	venv/bin/python -m flask --app lambda_function:app --debug run


.PHONY: format
format: deps-dev
	venv/bin/python -m black .
	venv/bin/python -m isort .


.PHONY: lint
lint: deps-dev
	venv/bin/python -m black . --check
	venv/bin/python -m flake8 .
	venv/bin/python -m isort . --check
	venv/bin/python -m mypy .


.PHONY: test
test: deps-dev
	venv/bin/python -m pytest -v
