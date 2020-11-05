from typing import Iterable


class CacheKeyManager:
    """Handles generating cache keys."""

    _PAINTING_PREPEND = "p"
    _ARTIST_PREPEND = "a"
    _EXHIBITIONS_PREPEND = "e"
    _ML_PREPEND = "m"
    _ARTIST_PAINTINGS_PREPEND = "ap"

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
        """Get a unique hash key for all exhibitions."""
        return CacheKeyManager._EXHIBITIONS_PREPEND

    @staticmethod
    def ml_cache_key() -> str:
        """Get a unique hash key all ml hashes."""
        return CacheKeyManager._ML_PREPEND

    @staticmethod
    def artist_paintings_cache_key(identities: Iterable[int]) -> str:
        """Get a unique hash key for artist's paintings."""
        identities_str = "_".join(str(i) for i in identities)
        return f"{CacheKeyManager._ARTIST_PAINTINGS_PREPEND}{identities_str}"
