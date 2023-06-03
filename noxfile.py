import nox


@nox.session
def tests(session):
    session.install("pytest")
    session.run("pytest")


@nox.session
def lint(session):
    session.install("black")
    session.install("ruff")
    session.install("mypy")
    session.run("black", "--check", ".")
    session.run("ruff", "check", ".")
    session.run("mypy", ".")


@nox.session
def format(session):
    session.install("black")
    session.install("ruff")
    session.run("black", ".")
    session.run("ruff", "--fix", ".")
