import json

from Utils.APIs import SignupAPI


def signup_user(email, password, validation_password, is_requesting_newsletter_signup, is_new_to_therapy):
    data_dic = {'email': email,
                'password': password,
                'validationPassword': validation_password,
                'isRequestingNewsletterSignup': is_requesting_newsletter_signup,
                'isNewToTherapy': is_new_to_therapy
                }
    response = SignupAPI.signup_user(json.dumps(data_dic))
    return response
