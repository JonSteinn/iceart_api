from typing import Callable

from flask import Blueprint


class BaseController(Blueprint):
    """Base controller type."""

    def __init__(self, prefix: str):
        assert prefix[0] == "/"
        super().__init__(prefix[1:], __name__, url_prefix=prefix)

    def add_route(self, path: str, callback: Callable, **options):
        """Add callback to a route."""
        self.add_url_rule(path, callback.__name__, callback, **options)
