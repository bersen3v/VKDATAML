from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class Group:
    id: int

    @classmethod
    def from_json(cls, data: Dict) -> "Group":
        return cls(
            id=data.get('id'),
        )

    def to_json(self) -> dict:
        data = {
            'id': self.id,
        }
        return data





