from typing import Iterable

from flask import Blueprint

from .demo_controller import demo


def all_blueprints() -> Iterable[Blueprint]:
    """Get all blueprints."""
    yield demo


__all__ = ["demo", "all_blueprints"]
