"""
@author Yumix_
@wiki https://github.com/imfeel/VimeApi/wiki
"""
import requests, logging

def check_data_on_error(data):
    try:
        if data["error"]["error_code"]:
            logging.error(f"Request have error: {data['error']['error_code']} - {data['error']['error_msg']}")
            return False
    except:
        return True
DEV_API  = "https://api.vimeworld.ru/"
class VimeApi: 
    def __init__(self, token):         
        self.token = token
    def check_token(tokencheck, type="AUTH"):
        data = requests.get(f"{DEV_API}misc/token/{tokencheck}?token={self.token}").json()

        if check_data_on_error(data):
            if data["valid"]:
                if data["type"] == type.upper:
                    logging.debug(f"Valid token: {token}:{type}")
                    return data

            logging.error(f"Invalid token, : {token}:{type}")
            return None
    def achievements(self):
        data = requests.get(f"{DEV_API}misc/achievements?token={self.token}").json()

        if check_data_on_error(data):
            return data
    def maps(self):
        data = requests.get(f"{DEV_API}misc/maps?token={self.token}").json()

        if check_data_on_error(data):
            return data
    def games(self):
        data = requests.get(f"{DEV_API}misc/maps?token={DEV_TOKEN}").json()

        if check_data_on_error(data):
            return data
    def match_list(before=0, after=1, count=5):
        if before:
            request = "before=" + str(before)
        else:
            request = "after=" + str(after)

        data = requests.get(f"{DEV_API}match/list?{request}&count={count}&token={self.token}").json()

        if check_data_on_error(data):
            return data
    def match_latest(self):
        data = requests.get(f"{DEV_API}match/latest?token={self.token}").json()

        if check_data_on_error(data):
            return data
    def match(self, id=246473141751119872):
        data = requests.get(f"{DEV_API}match/{id}?token={self.token}").json()

        if check_data_on_error(data):
            return data
    def online_staff(self):
        data = requests.get(f"{DEV_API}online/staff?token={self.token}").json()

        if check_data_on_error(data):
            return data
    def online_streams(self):
        data = requests.get(f"{DEV_API}online/streams?token={self.token}").json()

        if check_data_on_error(data):
            return data
    def online(self): 
        data = requests.get(f"{DEV_API}online?token={self.token}").json()

        if check_data_on_error(data):
            return data
    def leaderboard(self, type="user", sort="lvl", size=100, offset=0):
        data = requests.get(f"{DEV_API}leaderboard/get/{type}/{sort}?size={size}&offset={offset}&token={self.token}").json()

        if check_data_on_error(data):
            return data
    def leaderboard_list(self):
        data = requests.get(f"{DEV_API}leaderboard/list?token={self.token}").json()

        if check_data_on_error(data):
            return data
    def guild(self, id=None, name=None, tag=None):
        request = "id=1"
        if id != None:
            request = "id=" +str(id)
        elif name != None:
            request = "name=" +str(name)
        elif tag != None:
            request = "tag=" +str(tag)

        data = requests.get(f"{DEV_API}match/list?{request}&token={self.token}").json()

        if check_data_on_error(data):
            return data
    def guild_search(self, what):
        data = requests.get(f"{DEV_API}guild/search?query={what}&token={self.token}").json()

        if check_data_on_error(data):
            return data
    def user_sessions(self, ids = [1, 2, 3, 4, 5]):
        data = requests.post(f"{DEV_API}user/session?token={self.token}", json=ids).json()

        if check_data_on_error(data):
            return data
    def user_matches(self, user=1):
        data = requests.get(f"{DEV_API}user/{user}/matches?token={self.token}").json()

        if check_data_on_error(data):
            return data
    def user_leaderboards(self, user=1):
        data = requests.get(f"{DEV_API}user/{user}/leaderboards?token={self.token}").json()

        if check_data_on_error(data):
            return data
    def user_achievements(self, user=1):
        data = requests.get(f"{DEV_API}user/{user}/achievements?token={self.token}").json()

        if check_data_on_error(data):
            return data
    def user_session(self, user=1):
        data = requests.get(f"{DEV_API}user/{user}/session?token={self.token}").json()

        if check_data_on_error(data):
            return data
    def user_friends(self, user=1):
        data = requests.get(f"{DEV_API}user/{user}/friends?token={self.token}").json()

        if check_data_on_error(data):
            return data
    def user(self, user=1):
        if isinstance(user, int):
            data = requests.get(f"{DEV_API}user/{user}?token={self.token}").json()
        else:
            request = ""
            for u in user:
                request += str(u) + ","

            data = requests.get(f"{DEV_API}user/{request}?token={self.token}").json()

        if check_data_on_error(data):
            return data
    def user_name(self, user="Yumix_"):
        data = requests.get(f"{DEV_API}user/name/{user}?token={self.token}").json()

        if check_data_on_error(data):
            return data
    def request_limit(self):
        data = requests.get(f"{DEV_API}online?token={self.token}").headers
        return {"X-RateLimit-Limit":       data["X-RateLimit-Limit"],
                "X-RateLimit-Remaining":   data["X-RateLimit-Remaining"],
                "X-RateLimit-Reset-After": data["X-RateLimit-Reset-After"]}
