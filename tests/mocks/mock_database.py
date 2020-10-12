from werkzeug.exceptions import BadRequest, NotFound


class Dict2Class:
    def __init__(self, **data):
        for key, val in data.items():
            if isinstance(val, dict):
                self.__dict__[key] = Dict2Class(**val)
            else:
                self.__dict__[key] = val


_PAINTING_MOCK_DATA = {
    0: {
        "_id": 0,
        "title": "m_title0",
        "info": "m_info0",
        "artist_id": 1,
        "file": "f1.jpg",
    },
    2: {
        "_id": 2,
        "title": "m_title2",
        "info": "m_info2",
        "artist_id": 1,
        "file": "f44.jpg",
    },
    7: {
        "_id": 7,
        "title": "m_title7",
        "info": "m_info7",
        "artist_id": 2,
        "file": "f133.jpg",
    },
}


def painting_find_one_or_404(search_data):
    if "_id" not in search_data or not isinstance(search_data["_id"], int):
        raise BadRequest()
    if search_data["_id"] not in _PAINTING_MOCK_DATA:
        raise NotFound()
    return _PAINTING_MOCK_DATA[search_data["_id"]]


def painting_find():
    return _PAINTING_MOCK_DATA.values()


_MOCK_FIELDS = {
    "painting": {"find_one_or_404": painting_find_one_or_404, "find": painting_find}
}


class MockDatabase(Dict2Class):
    def __init__(self):
        super().__init__(**_MOCK_FIELDS)


class MockMongo:
    def __init__(self):
        self.db = MockDatabase()

    def init_app(self, app):
        """Fake initialize app."""
