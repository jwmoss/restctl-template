.PHONY: render test clean

SMOKE_DIR ?= /tmp/restctl-template-smoke
SMOKE_PROJECT ?= acme-api-cli

render:
	rm -rf "$(SMOKE_DIR)/$(SMOKE_PROJECT)"
	uvx cookiecutter --no-input -o "$(SMOKE_DIR)" .

test: render
	cd "$(SMOKE_DIR)/$(SMOKE_PROJECT)" && git init -q && git add . && git -c user.email=smoke@example.com -c user.name=smoke commit -qm "Initial commit" && make check

clean:
	rm -rf "$(SMOKE_DIR)/$(SMOKE_PROJECT)"
