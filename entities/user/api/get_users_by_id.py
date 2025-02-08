from entities.user.api.constants.user_fields import fields
from shared.api.http_get import http_get
from shared.constants import vk_api_base_url, api_v


def get_users_by_id(access_token: str, user_ids: list[str], query_fields: list[str] = fields) -> dict:
    url = f"{vk_api_base_url}/users.get"
    params = {
        "access_token": access_token,
        "v": api_v,
        "fields": ",".join(query_fields),
        "user_ids": user_ids,
    }
    result = http_get(url, params)
    return result


