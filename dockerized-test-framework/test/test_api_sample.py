import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.mark.smoke
def test_get_users():

    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200


@pytest.mark.regression
def test_get_single_user():

    response = requests.get(f"{BASE_URL}/users/1")
    print(response.json())
    
    assert response.status_code == 200
    assert response.json()["id"] == 1


@pytest.mark.regression
def test_create_post():

    payload = {
        "title": "pytest",
        "body": "testing",
        "userId": 1
    }

    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload
    )

    assert response.status_code == 201
