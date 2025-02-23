from entities.user.api.get_users_by_id import get_users_by_id
from entities.user.model.user import User
from shared.constants import vk_api_token


def get_user_model_by_id(id: str) -> User:
    user_data = get_users_by_id(access_token=vk_api_token, user_ids=[id])
    user = User.from_json(user_data['data']['response'][0])
    return user
