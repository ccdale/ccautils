"""Nox file for ccautils module."""
import tempfile

import nox

nox.options.sessions = "lint", "tests", "safety"
locations = "ccautils", "noxfile.py", "tests", "docs/conf.py"


def install_with_constraints(session, *args, **kwargs):
    """Constraints for packages installed.

    Args:
        session: nox session
        args: args
        kwargs: kwargs
    """
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


@nox.session(python=["3.6", "3.7", "3.8"])
def tests(session):
    """Nox session for pytest.

    Args:
        session: nox session
    """
    # args = session.posargs or ["--cov", "-m", "not ask"]
    args = session.posargs
    session.run("poetry", "install", "--no-dev", external=True)
    install_with_constraints(session, "coverage[toml]", "pytest", "pytest-cov")
    session.run("pytest", *args)


@nox.session(python=["3.8"])
def lint(session):
    """Nox session for linting.

    Args:
        session: nox session
    """
    args = session.posargs or locations
    install_with_constraints(
        session,
        "flake8",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
        "darglint",
    )
    session.run("flake8", *args)


@nox.session(python="3.8")
def safety(session):
    """Nox session for safety.

    Args:
        session: nox session
    """
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install("safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox.session(python=["3.8"])
def docs(session):
    """Nox session for documention.

    Args:
        session: nox session
    """
    session.run("poetry", "install", "--no-dev", external=True)
    install_with_constraints(
        session, "sphinx", "recommonmark", "sphinx-autodoc-typehints"
    )
    session.run("sphinx-build", "docs", "docs/_build")


@nox.session(python="3.8")
def coverage(session):
    """Upload coverage data.

    Args:
        session: nox session
    """
    install_with_constraints(session, "coverage[toml]", "codecov")
    session.run("coverage", "xml", "--fail-under=0")
    session.run("codecov", *session.posargs)
