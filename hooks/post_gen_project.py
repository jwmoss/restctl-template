import os
import pathlib
import shutil


REMOVE_PATHS = [
    "{% if cookiecutter.homebrew_package_type == 'none' %}.github/workflows/release.yml{% endif %}",
]

for raw_path in REMOVE_PATHS:
    path = raw_path.strip()
    if not path:
        continue
    p = pathlib.Path(path)
    if not p.exists():
        continue
    if p.is_dir():
        shutil.rmtree(p)
    else:
        p.unlink()

print("")
print("Generated {{ cookiecutter.project_slug }}")
print("")
print("Next steps:")
print("  cd {{ cookiecutter.project_slug }}")
print("  git init")
print("  go mod tidy")
print("  make check")
print("  {{ cookiecutter.binary_name }} config init --base-url {{ cookiecutter.api_base_url }}")
print("")
if "{{ cookiecutter.homebrew_package_type }}" != "none":
    print("Homebrew:")
    print("  Create or verify https://github.com/{{ cookiecutter.homebrew_tap_owner }}/{{ cookiecutter.homebrew_tap_repo }}")
    print("  Add HOMEBREW_TAP_TOKEN as a repository secret before tagging releases.")
    print("")
