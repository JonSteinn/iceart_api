class CacheKeyManager:
    """Handles generating cache keys."""

    # pylint: disable=too-few-public-methods

    _PAINTING_PREPEND = "p"

    @staticmethod
    def painting_id_cache_key(identity: int) -> str:
        """Get a unique hash key for painting by its id."""
        return f"{CacheKeyManager._PAINTING_PREPEND}{identity}"
