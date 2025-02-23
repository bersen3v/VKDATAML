from entities.group.api.get_groups_by_id import get_groups_by_id
from entities.group.model.group import Group
from shared.constants import vk_api_token


def get_group_model_by_id(id: str | int) -> Group:
    group_data = get_groups_by_id(access_token=vk_api_token, group_ids=[id])
    group = Group.from_json(group_data['data']['response']['groups'][0])
    return  group