import threading

from jane.database import client, noxarion as afk_collection



INSERTION_LOCK = threading.RLock()

AFK_USERS = {}


class AFK:
    def __init__(self, user_id, reason="", is_afk=True):
        self.user_id = user_id
        self.reason = reason
        self.is_afk = is_afk

    def __repr__(self):
        return "afk_status for {}".format(self.user_id)


def is_afk(user_id):
    return user_id in AFK_USERS


def check_afk_status(user_id):
    afk_user = afk_collection.find_one({"user_id": user_id})
    return afk_user


def set_afk(user_id, reason=""):
    with INSERTION_LOCK:
        curr = afk_collection.find_one({"user_id": user_id})
        if not curr:
            curr = AFK(user_id, reason, True)
            afk_collection.insert_one(curr.__dict__)
        else:
            curr['is_afk'] = True
            afk_collection.update_one({"user_id": user_id}, {"$set": curr})

        AFK_USERS[user_id] = reason


def rm_afk(user_id):
    with INSERTION_LOCK:
        curr = afk_collection.find_one({"user_id": user_id})
        if curr:
            if user_id in AFK_USERS:  # sanity check
                del AFK_USERS[user_id]

            afk_collection.delete_one({"user_id": user_id})
            return True

        return False


def toggle_afk(user_id, reason=""):
    with INSERTION_LOCK:
        curr = afk_collection.find_one({"user_id": user_id})
        if not curr:
            curr = AFK(user_id, reason, True)
            afk_collection.insert_one(curr.__dict__)
        elif curr['is_afk']:
            curr['is_afk'] = False
        else:
            curr['is_afk'] = True
        afk_collection.update_one({"user_id": user_id}, {"$set": curr})


def __load_afk_users():
    global AFK_USERS
    all_afk = afk_collection.find({"is_afk": True})
    AFK_USERS = {user['user_id']: user['reason'] for user in all_afk}


__load_afk_users()
