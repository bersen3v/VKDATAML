from entities.group.api.get_group_subscribers_by_id import get_group_subscribers_by_id
from entities.group.model.group import Group
from entities.user.api.constants.user_fields import primary_fields
from entities.user.model.user import User
from shared.constants import vk_api_token
from shared.datasets.methods.save_to_datasets import save_to_datasets_as_json


def get_subscribers_list(group_id: int | str, count:int = 1000, offset: int = 0, query_fields: list[str] = primary_fields) -> list[User]:
    data = get_group_subscribers_by_id(access_token=vk_api_token, group_id=group_id, query_fields=query_fields, offset = offset, count=count)
    # save_to_datasets_as_json(directory=str(group_id), name="group_subscribers", data=data)
    if 'error' not in data['data']:
        subscribers = data['data']['response']['items']
        subscribers_as_users = []
        for friend in subscribers:
            subscribers_as_users.append(User.from_json(friend))
        return subscribers_as_users
    return []