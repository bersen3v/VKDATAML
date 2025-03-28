import json
from dataclasses import dataclass

@dataclass
class City:
    id: int
    title: str

    def to_json(self) -> dict:
        data = {
            'id': self.id,
            'title': self.title
        }
        return data

    @classmethod
    def from_json(cls, data: dict) -> "City":
        if data is None:
            return None
        return cls(
            id=data.get('id'),
            title=data.get('title')
        )
