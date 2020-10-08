from iceart.services import IPaintingService


class MockPaintingService(IPaintingService):
    def get_painting_by_id(self, painting_id: int) -> dict:
        return {"_id": painting_id, "title": "m_title", "info": "m_info"}
