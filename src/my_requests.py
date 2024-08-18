import json

import requests


def post_requests(url, headers, payload):
    post_req = requests.post(url=url, headers=headers, data=json.dumps(payload))
    return post_req


def put_requests(url, headers, payload):
    post_req = requests.put(url=url, headers=headers, data=json.dumps(payload))
    return post_req


def del_requests(url, headers):
    del_req = requests.put(url=url, headers=headers)
    return del_req
