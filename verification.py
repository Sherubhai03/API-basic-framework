def verify_status(response, e_data):
    print("Status Code is ", response.status_code)
    assert response.status_code == e_data, "Failed ER!=AR"
