from entities.user.api.constants.user_fields import fields
from shared.api.http_get import http_get
from shared.constants import vk_api_base_url, api_v


# Возвращает json со всеми друзьями пользователя
# по умолчанию: максимум 5к человек
# по умолчанию: набор полей fields
def get_user_friends_by_id(access_token: str, user_id: int, count: int = 5000, query_fields: list[str] = fields) -> dict:
    url = f"{vk_api_base_url}/friends.get"
    params = {
        "access_token": access_token,
        "v": api_v,
        "count": count,
        "fields": ','.join(query_fields),
        "user_id": user_id,
    }
    result = http_get(url, params)
    return result

