from iceart.models import ImageViewModel, PaintingDto
from iceart.services import IMachineLearningService, IPaintingService


def mockymock(self):
    self.id = 5
    self.title = "t"
    self.info = "i"
    self.image = "img"


old_init = PaintingDto.__init__
PaintingDto.__init__ = mockymock
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
