.PHONY: render test

SMOKE_DIR ?= $(shell mktemp -d)

render:
	uvx --from cookiecutter==2.7.1 cookiecutter --no-input -o "$(SMOKE_DIR)" .

test:
	uv run --no-project --with cookiecutter==2.7.1 python scripts/check.py
