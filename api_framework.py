import pytest
import allure

from src.urls import *
from src.headers import *
from src.payload import *
from src.my_requests import *
from src.verification import verify_status


def post_positive():
    post_response = post_requests(url=post_url(), headers=post_headers(), payload=post_payload())
    verify_status(post_response, 200)
    fnamee = post_response.json()["booking"]["firstname"]
    lnamee = post_response.json()["booking"]["lastname"]
    id = post_response.json()["bookingid"]
    print("Created ", id, fnamee, lnamee)
    return id


def put_positive():
    puturl = put_url() + str(post_positive())
    put_response = put_requests(url=puturl, headers=put_headers(), payload=put_payload())
    verify_status(put_response, 200)
    fnamee = put_response.json()["firstname"]
    lnamee = put_response.json()["lastname"]
    print("Updated " + fnamee, lnamee, puturl)
    return puturl


def test_del_positive():
    del_url = put_positive()
    del_response = requests.delete(url=del_url, headers=del_headers())
    print("Deleted")
    verify_status(del_response, 201)
