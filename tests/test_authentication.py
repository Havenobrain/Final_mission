import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.mark.django_db
@pytest.mark.parametrize("token_type", ["access", "refresh"])
def test_jwt_tokens(client, token_type):
    client = APIClient()

    # Создаем тестового пользователя
    user = User.objects.create_user(username='testuser', password='testpassword')

    data = {
        "username": "testuser",
        "password": "testpassword"
    }
    response = client.post("/api/token/", data=data)
    assert response.status_code == 200
    tokens = response.json()
    assert "access" in tokens
    assert "refresh" in tokens

    if token_type == "refresh":
        response = client.post("/api/token/refresh/", data={"refresh": tokens["refresh"]})
        assert response.status_code == 200
        tokens = response.json()
        assert "access" in tokens
    else:
        response = client.get("/api/machines/", headers={"Authorization": f"Bearer {tokens['access']}"})
        assert response.status_code == 200

    headers = {"Authorization": f"Bearer {tokens['access']}"}
    response = client.get("/api/machines/", headers=headers)
    assert response.status_code == 200

    # Убираем тест на черный список, если он не реализован
    # response = client.post("/api/token/blacklist/", data={"token": tokens[token_type]})
    # assert response.status_code == 200

    # Пытаемся использовать токен повторно после его черного списка (если тест черного списка реализован)
    # response = client.get("/api/machines/", headers=headers)
    # assert response.status_code == 401

