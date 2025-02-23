from dataclasses import dataclass
from typing import Dict, Optional
from entities.group.methods.get_subscribers_list import get_subscribers_list
from entities.user.api.constants.user_fields import primary_fields
from entities.user.model.user import User





@dataclass
class Group:
    id: int

    @classmethod
    def from_json(cls, data: Dict) -> "Group":
        return cls(
            id=data.get('id'),
        )

    def get_subscribers_list(self, count:int = 1000, offset: int = 0, query_fields: list[str] = primary_fields) -> list[User]:
        subs = get_subscribers_list(self.id, count, offset, query_fields)
        return subs

    def to_json(self) -> dict:
        data = {
            'id': self.id,
        }
        return data





