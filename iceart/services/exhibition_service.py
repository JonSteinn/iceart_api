import abc
from typing import Iterator, List

from geopy.distance import distance

from ..models.exhibition import (
    Exhibition,
    ExhibitionDto,
    ExhibitionsDto,
    ExhibitionViewModel,
)
from ..repositories import IExhibitionRepository


class IExhibitionService(abc.ABC):
    """Interface for exhibition service."""

    # pylint: disable=too-few-public-methods

    @abc.abstractmethod
    def get_all_nearby_exhibitions(self, data: dict) -> ExhibitionsDto:
        """Get all nearby exhibtions."""


class ExhibitionService(IExhibitionService):
    """Exhibition service."""

    # pylint: disable=too-few-public-methods

    _MAX_KM_DISTANCE = 15

    def __init__(self, exhibition_repository: IExhibitionRepository):
        self._exhibition_repository = exhibition_repository

    def get_all_nearby_exhibitions(self, data: dict) -> ExhibitionsDto:
        view_model = ExhibitionViewModel(data)
        all_exhibitions = self._exhibition_repository.get_all_exhibitions()
        return ExhibitionsDto(
            ExhibitionService._extract_nearby_exhibitions(view_model, all_exhibitions)
        )

    @staticmethod
    def _extract_nearby_exhibitions(
        view_model: ExhibitionViewModel, all_exhibitions: List[Exhibition]
    ) -> Iterator[ExhibitionDto]:
        base_loc = (view_model.latitude, view_model.longitude)
        return (
            ExhibitionDto(exhibition)
            for exhibition in all_exhibitions
            if distance(base_loc, (exhibition.latitude, exhibition.longitude)).km
            < ExhibitionService._MAX_KM_DISTANCE
        )
