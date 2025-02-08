from entities.user.model.user import User

def friends_binary_search(user: User, user_list: list[User]) -> int:
    l: int = 0
    r: int = len(user_list)-1

    while l<=r:
        mid: int = (l+r)//2
        if user_list[mid].id == user.id:
            return mid
        if user_list[mid].id > user.id:
            r = mid - 1
        else:
            l = mid + 1

    return -1