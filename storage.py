from abc import ABC, abstractmethod
import json


class Storage(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def save(self, data):
        pass


class JsonFileStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)


class MemoryStorage(Storage):
    def __init__(self, initial=None):
        self.data = initial or {}

    def load(self):
        return dict(self.data)

    def save(self, data):
        self.data = dict(data)