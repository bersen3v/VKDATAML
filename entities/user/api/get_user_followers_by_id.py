
from entities.user.api.constants.user_fields import fields
from entities.user.model.user import User
from shared.api.http_get import http_get
from shared.constants import vk_api_base_url, api_v


def get_user_followers_by_id(access_token: str, user_id: int, query_fields: list[str] = fields) -> User:
    url = f"{vk_api_base_url}/users.getFollowers"
    params = {
        "access_token": access_token,
        "v": api_v,
        "fields": ",".join(query_fields),
        "user_id": user_id,
    }
    result = http_get(url, params)
    return result


