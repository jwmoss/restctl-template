import re
import sys


def require(pattern: str, value: str, name: str) -> None:
    if not re.match(pattern, value):
        print(f"ERROR: {name}={value!r} must match {pattern!r}")
        sys.exit(1)


require(r"^[a-z][a-z0-9-]*[a-z0-9]$", "{{ cookiecutter.project_slug }}", "project_slug")
require(r"^[a-z][a-z0-9-]*[a-z0-9]$", "{{ cookiecutter.binary_name }}", "binary_name")
require(r"^[A-Z][A-Z0-9_]*[A-Z0-9]$", "{{ cookiecutter.env_prefix }}", "env_prefix")
require(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/.+", "{{ cookiecutter.module_path }}", "module_path")
require(r"^/[A-Za-z0-9_./{}-]*$", "{{ cookiecutter.health_path }}", "health_path")
require(r"^/[A-Za-z0-9_./{}-]*$", "{{ cookiecutter.resource_path }}", "resource_path")
