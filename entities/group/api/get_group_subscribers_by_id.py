from entities.user.api.constants.user_fields import fields
from shared.api.http_get import http_get
from shared.constants import vk_api_base_url, api_v


def get_group_subscribers_by_id(access_token: str, group_id: int, count: int = 1000, offset: int = 0, query_fields: list[str] = fields) -> dict:
    url = f"{vk_api_base_url}/groups.getMembers"
    params = {
        "access_token": access_token,
        "v": api_v,
        "offset":offset,
        "count":count,
        "fields": ",".join(query_fields),
        "sort":"id_asc",
        "group_id": group_id,
    }
    result = http_get(url, params)
    return result
