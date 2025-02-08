from entities.user.api.get_user_friends_by_id import get_user_friends_by_id
from entities.user.api.constants.user_fields import fields
from entities.user.model.user import User
from shared.constants import vk_api_token
from shared.datasets.methods.save_to_datasets import save_to_datasets_as_json


def get_friends_list(user_id: int, query_fields: list[str] = fields, count : int = 5000) -> list[User]:
    data = get_user_friends_by_id(vk_api_token, user_id=user_id, query_fields=query_fields, count=count)
    # save_to_datasets_as_json(directory=str(user_id), name="user_friends", data=data)
    if data['success']:
        if 'error' not in data['data']:
            friends = data['data']['response']['items']
            friends_as_users = []
            for friend in friends:
                friends_as_users.append(User.from_json(friend))
            return friends_as_users
    print('пятисотит')
    return []