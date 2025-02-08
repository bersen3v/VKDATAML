from dataclasses import dataclass
from typing import Dict, Optional

from entities.user.sub_entities.career import Career
from entities.user.sub_entities.city import City
from entities.user.sub_entities.country import Country
from entities.user.sub_entities.education import Education


@dataclass
class User:
    id: int
    domain: str
    first_name: str
    last_name: str
    deactivated: str

    about: str
    activities: str
    bdate: str
    books: str
    city: City
    education: Education
    country: Country

    career: list[Career]
    can_post: int
    photo_max_orig: str
    is_closed: bool

    @classmethod
    def from_json(cls, data: Dict) -> "User":
        return cls(
            id=data.get('id'),
            domain=data.get('domain'),
            deactivated=data.get('deactivated'),
            photo_max_orig=data.get('photo_max_orig'),
            first_name=data.get('first_name'),
            city = City.from_json(data.get('city')),
            education=Education.from_json(data.get('education')),
            country = Country.from_json(data.get('country')),
            last_name=data.get('last_name'),
            is_closed=bool(data.get('is_closed')),
            career = [Career.from_json(val) for val in data.get('career',[])],
            about = data.get('about'),
            activities = data.get('activities'),
            bdate = data.get('bdate'),
            books = data.get('books'),
            can_post = data.get('can_post'),
        )

    def to_json(self) -> dict:
        career_data = [career.to_json() for career in self.career]
        education_data = self.education.to_json() if self.education is not None else None
        city_data = self.city.to_json()['title'] if self.city is not None else None
        country_data = self.country.to_json() if self.country is not None else None
        data = {
            'id': self.id,
            'domain': self.domain,
            'deactivated': self.deactivated,
            'photo_max_orig': self.photo_max_orig,
            'first_name': self.first_name,
            'city': city_data,
            'education': education_data,
            'country': country_data,
            'last_name': self.last_name,
            'is_closed': self.is_closed,
            'career': career_data,
            'about': self.about,
            'activities': self.activities,
            'bdate': self.bdate,
            'books': self.books,
            'can_post': self.can_post
        }
        return data





