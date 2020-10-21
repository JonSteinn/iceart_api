import traceback
from typing import Callable

from flask import Response
from werkzeug.exceptions import HTTPException


class ErrorHandler:
    """Error handler class."""

    #  pylint: disable = too-few-public-methods

    def __init__(self, debug: bool):
        self.debug = debug

    def get_handler(self) -> Callable[[Exception], Response]:
        """Get error handler."""
        return (
            ErrorHandler._debug_handler
            if self.debug
            else ErrorHandler._production_handler
        )

    @staticmethod
    def _debug_handler(exc: Exception) -> Response:
        if isinstance(exc, HTTPException):
            return Response(
                status=exc.code,
                mimetype="application/json",
            )
        print("=" * 40)
        traceback.print_exc()
        print("=" * 40)
        return Response(
            status=500,
            mimetype="application/json",
        )

    @staticmethod
    def _production_handler(exc: Exception) -> Response:
        return Response(
            status=exc.code if isinstance(exc, HTTPException) else 500,
            mimetype="application/json",
        )
