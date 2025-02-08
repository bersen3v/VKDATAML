import json
from dataclasses import dataclass
from typing import Optional

@dataclass
class Career:
    group_id: int
    company: str
    city_id: int
    city_name: str
    from_year: int
    until_year: int
    position: str

    @classmethod
    def from_json(cls, data: dict) -> "Career":
        return cls(
            group_id=data.get('group_id'),
            company=data.get('company'),
            city_id=data.get('city_id'),
            city_name=data.get('city_name'),
            from_year=data.get('from'),
            until_year=data.get('until'),
            position=data.get('position')
        )

    def to_json(self) -> dict:
        data = {
            'group_id': self.group_id,
            'company': self.company,
            'city_id': self.city_id,
            'city_name': self.city_name,
            'from': self.from_year,
            'until': self.until_year,
            'position': self.position
        }
        return data

