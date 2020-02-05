# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
import json

import nox


with open('./.vscode/settings.json') as settings_file:
    settings = json.load(settings_file)


target_versions = ['3.5', '3.6', '3.7', '3.8']
nox.options.reuse_existing_virtualenvs = True


@nox.session()
def lint(session):
    session.install('-e', '.[lint]')
    session.run(
        "pylint",
        *settings["python.linting.pylintArgs"],
        "setup.py",
        "noxfile.py",
        "unipixel")
