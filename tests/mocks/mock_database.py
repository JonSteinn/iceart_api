class Dict2Class:
    def __init__(self, **data):
        for key, val in data.items():
            if isinstance(val, dict):
                self.__dict__[key] = Dict2Class(**val)
            else:
                self.__dict__[key] = val


class MockDatabase(Dict2Class):
    _MOCK_FIELDS = {
        "painting": {
            "find_one_or_404": lambda x: {
                "_id": x["_id"],
                "title": "m_title",
                "info": "m_info",
            }
        }
    }

    def __init__(self):
        super().__init__(**MockDatabase._MOCK_FIELDS)
