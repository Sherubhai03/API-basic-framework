from src.token import *


def post_headers():
    headers = {"Content-Type": "application/json"}
    return headers


def put_headers():
    headers = {"Content-Type": "application/json",
               "cookie": "token=" + create_token()
               }
    print(create_token())
    return headers


def del_headers():
    headers = {"Content-Type": "application/json",
               "cookie": "token=" + create_token()
               }
    print(create_token())
    return headers
