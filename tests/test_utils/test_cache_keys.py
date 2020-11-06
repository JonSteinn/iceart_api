from iceart.utils import CacheKeyManager


def test_painting_id_cache_key():
    assert CacheKeyManager.painting_id_cache_key(3) == "p3"


def test_artist_id_cache_key():
    assert CacheKeyManager.artist_id_cache_key(1513) == "a1513"


def test_exhibitions_cache_key():
    assert CacheKeyManager.exhibitions_cache_key() == "e"


def test_ml_cache_key():
    assert CacheKeyManager.ml_cache_key() == "m"


def test_artist_paintings_cache_key():
    assert CacheKeyManager.artist_paintings_cache_key(4) == "ap4"
