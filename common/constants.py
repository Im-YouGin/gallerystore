from enum import Enum


class ChoicesEnum(Enum):
    def __str__(self):
        return self.value

    @classmethod
    def choices(cls):
        return [(x.value, x.name.replace("_", " ").title()) for x in cls]
