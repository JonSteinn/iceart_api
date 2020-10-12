from iceart.setup.app import create_app
from iceart.setup.config import TestingConfig

from .mock_database import MockMongo


class MockApp:

    _JSON_REQ_HEADERS = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    def __init__(self):
        self.app = create_app(MockMongo(), TestingConfig())

    def make_get_request(self, path, headers=None):
        if headers is None:
            headers = MockApp._JSON_REQ_HEADERS
        with self.app.app_context(), self.app.test_client() as client:
            res = client.get(path, headers=headers)
        return res

    def make_post_request(self, path, body, headers=None):
        if headers is None:
            headers = MockApp._JSON_REQ_HEADERS
        with self.app.app_context(), self.app.test_client() as client:
            res = client.post(path, headers=headers, data=body)
        return res
