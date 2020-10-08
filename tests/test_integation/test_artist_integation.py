import json

from iceart.setup.app import create_app
from iceart.setup.config import TestingConfig

from ..mocks.mock_database import MockMongo

_HEADER = {"Accept": "application/json", "Content-Type": "application/json"}


def test_painting_integration_get_painting_by_id_ok():
    # Arrange
    app = create_app(MockMongo(), TestingConfig())
    _id = 2
    expected = {"_id": _id, "title": "m_title2", "info": "m_info2"}

    # Act
    with app.app_context(), app.test_client() as client:
        res = client.get(f"/painting/{_id}", headers=_HEADER)

    # Assert
    assert res.status_code == 200
    assert res.headers["Content-Type"] == "application/json"
    assert json.loads(res.get_data(as_text=True)) == expected


def test_painting_integration_get_painting_by_id_not_found():
    # Arrange
    app = create_app(MockMongo(), TestingConfig())
    _id = 4444

    # Act
    with app.app_context(), app.test_client() as client:
        res = client.get(f"/painting/{_id}", headers=_HEADER)

    # Assert
    assert res.status_code == 404
    assert res.headers["Content-Type"] == "application/json"
