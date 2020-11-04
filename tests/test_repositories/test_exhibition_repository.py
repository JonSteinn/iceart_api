from iceart.repositories import ExhibitionRepository

from ..mocks.mock_cache import MockCache
from ..mocks.mock_database import MockDatabase


def test_exhibition_repository_get_all_exhibitions():
    # Arrange
    repo = ExhibitionRepository(MockDatabase(), MockCache())

    # Act
    allSorted = sorted(repo.get_all_exhibitions(), key=lambda p: p.identity)
    allCachedSorted = sorted(repo.get_all_exhibitions(), key=lambda p: p.identity)

    # Assert
    assert [p.identity for p in allSorted] == [0, 1, 2]
    assert [p.identity for p in allCachedSorted] == [0, 1, 2]
