class CacheKeyManager:
    """Handles generating cache keys."""

    _PAINTING_PREPEND = "p"
    _ARTIST_PREPEND = "a"
    _EXHIBITIONS_PREPEND = "e"

    @staticmethod
    def painting_id_cache_key(identity: int) -> str:
        """Get a unique hash key for painting by its id."""
        return f"{CacheKeyManager._PAINTING_PREPEND}{identity}"

    @staticmethod
    def artist_id_cache_key(identity: int) -> str:
        """Get a unique hash key for artist by its id."""
        return f"{CacheKeyManager._ARTIST_PREPEND}{identity}"

    @staticmethod
    def exhibitions_cache_key() -> str:
        """Get a unique hash key all exhibitions."""
        return CacheKeyManager._EXHIBITIONS_PREPEND
