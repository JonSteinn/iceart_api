from typing import List

from iceart.models import Painting, PaintingViewModel
from iceart.repositories import IPaintingRepository


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
