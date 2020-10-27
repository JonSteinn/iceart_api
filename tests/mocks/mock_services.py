from iceart.models import (
    ArtistDto,
    Exhibition,
    ExhibitionDto,
    ExhibitionsDto,
    ImageViewModel,
    PaintingDto,
)
from iceart.services import (
    IArtistService,
    IExhibitionService,
    IMachineLearningService,
    IPaintingService,
)


def mock_painting_dto_constructor(self):
    self.id = 5
    self.title = "t"
    self.info = "i"
    self.image = "img"


def mock_artist_dto_constructor(self):
    self.id = 665
    self.title = "t"
    self.info = "i"
    self.image = "img"


old_init = PaintingDto.__init__
PaintingDto.__init__ = mock_painting_dto_constructor
_FAKE_PAINTING_DTO = PaintingDto()
PaintingDto.__init__ = old_init

old_init = ArtistDto.__init__
ArtistDto.__init__ = mock_artist_dto_constructor
_FAKE_ARTIST_DTO = ArtistDto()
PaintingDto.__init__ = old_init


class MockPaintingService(IPaintingService):
    def get_painting_by_id(self, painting_id: int) -> PaintingDto:
        return _FAKE_PAINTING_DTO

    def get_akin_painting(self, data: dict) -> PaintingDto:
        return _FAKE_PAINTING_DTO


class MockArtistService(IArtistService):
    def get_artist_by_id(self, artist_id: int) -> ArtistDto:
        return _FAKE_ARTIST_DTO


class MockMachineLearningService(IMachineLearningService):
    def get_most_smilar_painting(self, image_vm: ImageViewModel) -> PaintingDto:
        return _FAKE_PAINTING_DTO


class MockExhibitionService(IExhibitionService):
    def get_all_nearby_exhibitions(self, data: dict) -> ExhibitionsDto:
        return ExhibitionsDto(
            (
                ExhibitionDto(
                    Exhibition(
                        {
                            "_id": 1,
                            "title": "m_title1",
                            "info": "m_info1",
                            "latitude": 64.145265,
                            "longitude": -21.945307,
                        }
                    )
                ),
                ExhibitionDto(
                    Exhibition(
                        {
                            "_id": 2,
                            "title": "m_title2",
                            "info": "m_info2",
                            "latitude": 64.15046,
                            "longitude": -21.950737,
                        }
                    )
                ),
            )
        )
