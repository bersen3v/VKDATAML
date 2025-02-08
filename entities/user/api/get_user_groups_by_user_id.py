from entities.user.model.user import User
from shared.api.http_get import http_get
from shared.constants import vk_api_base_url, api_v


def get_user_groups_by_user_id(access_token: str, user_id: int) -> User:
    url = f"{vk_api_base_url}/groups.get"
    params = {
        "access_token": access_token,
        "v": api_v,
        "extended": 1,
        "user_id": user_id,
    }
    result = http_get(url, params)
    return result

