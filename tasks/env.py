from invoke.context import Context
from invoke.tasks import task

from tasks.common import VENV_PREFIX


@task
def clean(ctx: Context) -> None:
    """Remove virtual environment"""
    ctx.run("rm -rf .venv", warn=True)


@task(optional=["no-pre-commit"])
def init(ctx: Context, with_pre_commit: bool = False) -> None:
    """Initialize virtual environment"""
    ctx.run("uv sync")
    if not with_pre_commit:
        setup_pre_commit_hook(ctx)


@task
def setup_pre_commit_hook(ctx: Context) -> None:
    """Setup pre-commit hook to automate check before git commit and git push"""
    ctx.run("git init")
    ctx.run(
        f"{VENV_PREFIX} pre-commit install -t pre-commit & "
        f"{VENV_PREFIX} pre-commit install -t pre-push & "
        f"{VENV_PREFIX} pre-commit install -t commit-msg &"
        f"{VENV_PREFIX} pre-commit autoupdate"
    )
