import json
from dataclasses import dataclass

@dataclass
class Education:
    university: int
    university_name: str
    faculty: int
    faculty_name: str
    graduation: int

    def to_json(self) -> dict:
        data = {
            'university': self.university,
            'university_name': self.university_name,
            'faculty': self.faculty,
            'faculty_name': self.faculty_name,
            'graduation': self.graduation
        }
        return data

    @classmethod
    def from_json(cls, data: dict) -> 'Education':
        if data is None:
            return None
        return cls(
            university=data.get('university'),
            university_name=data.get('university_name'),
            faculty=data.get('faculty'),
            faculty_name=data.get('faculty_name'),
            graduation=data.get('graduation')
        )
