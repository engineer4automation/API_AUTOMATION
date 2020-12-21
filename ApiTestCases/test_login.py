import json
import jsonpath
import pytest
import scope as scope

from Utils.Calls import SignupApiCall
from Utils.Calls import LoginApiCall
from Utils.Calls import GenericMethods as Data

authorization = None


@pytest.mark.order(6)
def test_invalid_login_email():
    response = LoginApiCall.login_user(Data.get_config('INVALID_EMAIL'), Data.get_config('VALID_PASSWORD'))

    # Validation
    response_json = json.loads(response.text)
    print(response_json)
    assert response.status_code == 500


@pytest.mark.order(7)
def test_login_invalid_password(login_email):
    response = LoginApiCall.login_user(login_email, Data.get_config('INVALID_PASSWORD'))

    # Validation
    response_json = json.loads(response.text)
    print(response_json)
    assert response.status_code == 400


@pytest.mark.order(8)
def test_valid_login(login_email):
    response = LoginApiCall.login_user(login_email, Data.get_config('VALID_PASSWORD'))

    global authorization
    authorization = response.headers["Authorization"]

    # Validation
    assert response.status_code == 200


@pytest.fixture()
def login_email():
    login_email = Data.get_email()
    response = SignupApiCall.signup_user(login_email, Data.get_config('VALID_PASSWORD'),
                                         Data.get_config('VALID_PASSWORD'), bool(True), bool(True))
    # Validation
    assert response.status_code == 200
    return login_email
