# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring
import nox


TARGET_VERSIONS = ['3.5', '3.6', '3.7', '3.8']
nox.options.reuse_existing_virtualenvs = True


@nox.session()
def lint(session):
    session.install('-e', '.[lint]')
    session.run(
        "pylint",
        "setup.py",
        "noxfile.py",
        "unipixel")
