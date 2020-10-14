from typing import List

from iceart.models import Exhibition, Painting, PaintingViewModel
from iceart.repositories import IExhibitionRepository, IPaintingRepository


class MockPaintingRepository(IPaintingRepository):
    def get_painting_by_id(self, painting_vm: PaintingViewModel) -> Painting:
        """Find user by its id."""
        return Painting(
            {
                "_id": painting_vm._id,
                "title": "m_title",
                "info": "m_info",
                "artist_id": 44,
                "file": "idfka",
            }
        )

    def get_all_paintings(self) -> List[Painting]:
        """Get all paintings."""
        return [
            Painting(
                {
                    "_id": 4,
                    "title": "m_title4",
                    "info": "m_info4",
                    "artist_id": 123,
                    "file": "idfka4",
                }
            ),
            Painting(
                {
                    "_id": 77,
                    "title": "m_title77",
                    "info": "m_info77",
                    "artist_id": 1361,
                    "file": "idfka77",
                }
            ),
        ]


class MockExhibitionRepository(IExhibitionRepository):
    def get_all_exhibitions(self) -> List[Exhibition]:
        return [
            Exhibition(
                {
                    "_id": 0,
                    "title": "m_title0",
                    "info": "m_info0",
                    "latitude": 65.6826,
                    "longitude": -18.0907,
                }
            ),
            Exhibition(
                {
                    "_id": 1,
                    "title": "m_title1",
                    "info": "m_info1",
                    "latitude": 64.145265,
                    "longitude": -21.945307,
                }
            ),
            Exhibition(
                {
                    "_id": 2,
                    "title": "m_title2",
                    "info": "m_info2",
                    "latitude": 64.15046,
                    "longitude": -21.950737,
                }
            ),
            Exhibition(
                {
                    "_id": 3,
                    "title": "m_title3",
                    "info": "m_info3",
                    "latitude": 64.125206,
                    "longitude": -21.813451,
                }
            ),
        ]
