from iceart.models import (
    Exhibition,
    ExhibitionDto,
    ExhibitionsDto,
    ImageViewModel,
    PaintingDto,
)
from iceart.services import (
    IExhibitionService,
    IMachineLearningService,
    IPaintingService,
)


def mock_painting_dto_constructor(self):
    self.id = 5
    self.title = "t"
    self.info = "i"
    self.image = "img"


old_init = PaintingDto.__init__
PaintingDto.__init__ = mock_painting_dto_constructor
_FAKE_DTO = PaintingDto()
PaintingDto.__init__ = old_init


class MockPaintingService(IPaintingService):
    def get_painting_by_id(self, painting_id: int) -> PaintingDto:
        return _FAKE_DTO

    def get_akin_painting(self, data: dict) -> PaintingDto:
        return _FAKE_DTO


class MockMachineLearningService(IMachineLearningService):
    def get_most_smilar_painting(self, image_vm: ImageViewModel) -> PaintingDto:
        return _FAKE_DTO


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
