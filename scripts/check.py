"""Render each supported package variant and verify its executable contracts."""

import argparse
import pathlib
import subprocess
import tempfile

from cookiecutter.main import cookiecutter

ROOT = pathlib.Path(__file__).resolve().parents[1]


def run(*args: str, cwd: pathlib.Path) -> None:
    subprocess.run(args, cwd=cwd, check=True)


def check(package: str) -> None:
    with tempfile.TemporaryDirectory(prefix="restctl-check-") as temp:
        project = pathlib.Path(cookiecutter(
            str(ROOT), no_input=True, output_dir=temp,
            extra_context={"homebrew_package_type": package},
        ))
        # "none" disables tap publication, not GitHub releases.
        assert (project / ".github/workflows/release.yml").is_file()
        files = [str(path) for path in project.rglob("*.go")]
        unformatted = subprocess.check_output(["gofmt", "-l", *files], text=True)
        if unformatted:
            raise RuntimeError(f"Unformatted generated files:\n{unformatted}")
        run("go", "mod", "tidy", "-diff", cwd=project)
        run("go", "vet", "./...", cwd=project)
        run("go", "test", "-count=1", "-timeout=2m", "./...", cwd=project)
        run("go", "build", "./...", cwd=project)
        result = subprocess.run(["goreleaser", "check"], cwd=project)
        # GoReleaser reserves exit 2 for valid, deprecated config. Formula is legacy.
        if result.returncode != 0 and not (package == "formula" and result.returncode == 2):
            result.check_returncode()
        run("go", "run", "github.com/rhysd/actionlint/cmd/actionlint@v1.7.12",
            ".github/workflows/ci.yml", ".github/workflows/release.yml", cwd=project)
        run("uvx", "--from", "zizmor==1.30.1", "zizmor", "--no-online-audits",
            "--no-progress", ".github/workflows", cwd=project)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--package", choices=["cask", "formula", "none"])
    args = parser.parse_args()
    for package in [args.package] if args.package else ["cask", "formula", "none"]:
        check(package)
