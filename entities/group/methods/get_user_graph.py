from entities.graph.methods.create_graph import create_graph
from entities.user.methods.get_friends_list import get_friends_list
from entities.user.methods.get_user_model_by_id import get_user_model_by_id


def get_user_graph(user_id: str):
    user = get_user_model_by_id(user_id)
    friends = get_friends_list(user_id=user.id)
    create_graph(object_id=user.id, users_list=friends)