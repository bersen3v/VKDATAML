from shared.api.http_get import http_get
from shared.constants import vk_api_base_url, api_v


def get_groups_by_id(access_token: str, group_ids: list[str]) -> dict:
    url = f"{vk_api_base_url}/groups.getById"
    params = {
        "access_token": access_token,
        "v": api_v,
        "group_ids": group_ids,
    }
    result = http_get(url, params)
    return result
