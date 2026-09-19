.PHONY: install test lint run package
install:
	python -m pip install -e '.[dev]'
test:
	pytest -q
lint:
	ruff check app tests
run:
	uvicorn app.main:app --reload --port 8080
package:
	bash scripts/package.sh
