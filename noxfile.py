"""nox file for ccautils module"""
import nox


@nox.session(python=["3.6", "3.7", "3.8"])
def tests(session):
    """nox session for pytest"""
    # args = session.posargs or ["--cov"]
    args = session.posargs
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


locations = "ccautils", "noxfile.py", "tests"


@nox.session(python=["3.8"])
def lint(session):
    """nox session for linting"""
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
    )
    session.run("flake8", *args)
