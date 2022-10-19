from json import load
from typing import Dict
from .utils import to_snake_case

class BaseDataClass:
    @classmethod
    def _load(cls, client, resource: Dict):
        instance = cls(client)
        for key, value in resource.items():
            snake_case_key = to_snake_case(key)
            if hasattr(instance, snake_case_key):
                setattr(instance, snake_case_key, value)
        instance.initialise()
        return instance

    def update(self, resource: Dict):
        for key, value in resource.items():
            snake_case_key = to_snake_case(key)
            if hasattr(self, snake_case_key) and getattr(self, snake_case_key) == None:
                setattr(self, snake_case_key, value)

    def initialise(self):
        # Intentionally left empty for subclasses to implement without error
        pass
