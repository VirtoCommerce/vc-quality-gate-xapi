class SharedData:
    data = {}

    @classmethod
    def set(cls, key, value):
        cls.data[key] = value

    @classmethod
    def get(cls, key):
        return cls.data.get(key)
