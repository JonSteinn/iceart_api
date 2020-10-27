import abc

from flask_pymongo.wrappers import Database

from ..models import Artist, ArtistViewModel


class IArtistRepository(abc.ABC):
    """Interface for artist service."""

    # pylint: disable=too-few-public-methods

    @abc.abstractmethod
    def get_artist_by_id(self, artist_vm: ArtistViewModel) -> Artist:
        """Find user by its id."""


class ArtistRepository(IArtistRepository):
    """Artist service."""

    # pylint: disable=too-few-public-methods

    def __init__(self, db: Database):
        self._db: Database = db

    def get_artist_by_id(self, artist_vm: ArtistViewModel) -> Artist:
        answer: dict = self._db.artist.find_one_or_404(artist_vm.search_key())
        return Artist(answer)
