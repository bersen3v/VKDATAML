from entities.graph.methods.create_graph import create_graph
from entities.group.api.get_groups_by_id import get_groups_by_id
from entities.group.methods.get_subscribers_list import get_subscribers_list
from entities.group.model.group import Group
from shared.constants import vk_api_token
import time
import json

file = open('shared/datasets/data/data_116131349/networkx_graph.json')
print(len(json.loads(file.read())['nodes']))
# start_time = time.time()
#
#
# group_data = get_groups_by_id(access_token=vk_api_token, group_ids=['ikitinfo'])
# group = Group.from_json(group_data['data']['response']['groups'][0])
# subscribers = []
# for i in range(5):
#     subscribers += get_subscribers_list(group_id=group.id, offset=1000*i)
# create_graph(object_id=group.id, users_list=subscribers)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(elapsed_time)
# user = User.from_json(get_user_by_id(access_token=vk_api_token))


