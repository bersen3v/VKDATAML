# file = open('shared/datasets/data/data_116131349/networkx_graph.json')
# data = json.loads(file.read())['nodes']
# df = pd.DataFrame(data=data)
# df.to_csv("ikit.csv")

# get_user_graph('303561841')



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

# group = get_by_id(id = "ikitinfo")
# subscribers = []
# for i in range(5):
#     subscribers += get_subscribers_list(group_id=group.id, offset=1000*i)
# create_graph(object_id=group.id, users_list=subscribers, count = 1000)


