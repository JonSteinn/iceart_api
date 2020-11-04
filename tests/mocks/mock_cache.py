class MockCache(dict):
    def set(self, key, val, *args, **kwargs):
        self[key] = val
