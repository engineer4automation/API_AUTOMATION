from Utils.Calls import GenericMethods
import requests
request_Session = requests.session()
# Configurations
url = GenericMethods.get_url() + "login"


def login_user(data):
    request_Session.headers.update({"Content-Type": "application/json;charset=UTF-8",
                                    "Accept": "application/json, text/plain, */*"
                                    })
    response = request_Session.post(url, data)
    return response
