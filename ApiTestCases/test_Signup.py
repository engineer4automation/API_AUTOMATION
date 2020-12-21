import json
import jsonpath
import pytest
from Utils.Calls import SignupApiCall
from Utils.Calls import GenericMethods as Data


@pytest.mark.order(1)
def test_create_new_user_invalid_email():
    response = SignupApiCall.signup_user(Data.get_config('INVALID_EMAIL'), Data.get_config('VALID_PASSWORD'),
                                         Data.get_config('VALID_PASSWORD'), bool(True), bool(True))
    # Validation
    response_json = json.loads(response.text)
    print(response_json)
    assert response.status_code == 500


@pytest.mark.order(2)
def test_create_new_user_empty_email():
    response = SignupApiCall.signup_user("", Data.get_config('VALID_PASSWORD'),
                                         Data.get_config('VALID_PASSWORD'), bool(True), bool(True))
    # Validation
    response_json = json.loads(response.text)
    print(response_json)
    assert response.status_code == 500


@pytest.mark.order(3)
def test_create_new_user_empty_passwords():
    response = SignupApiCall.signup_user(Data.get_email(), "",
                                         "", bool(True), bool(True))
    # Validation
    response_json = json.loads(response.text)
    print(response_json)
    assert response.status_code == 500


@pytest.mark.order(4)
def test_create_new_user_passwords_mismatch():
    response = SignupApiCall.signup_user(Data.get_email(), Data.get_config('VALID_PASSWORD'),
                                         Data.get_config('INVALID_PASSWORD'), bool(True), bool(True))
    # Validation
    response_json = json.loads(response.text)
    print(response_json)
    assert response.status_code == 500


@pytest.mark.order(5)
def test_create_new_user():
    response = SignupApiCall.signup_user(Data.get_email(), Data.get_config('VALID_PASSWORD'),
                                         Data.get_config('VALID_PASSWORD'), bool(True), bool(True))
    # Validation
    assert response.status_code == 200
