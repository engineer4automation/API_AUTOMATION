import json

from Utils.APIs import LoginAPI


def login_user(email, password):
    data_dic = {'email': email,
                'password': password
                }
    response = LoginAPI.login_user(json.dumps(data_dic))
    return response
