import pytest
from YouGileApi import YouGileAPI

# Позитивный тест (создание проекта)
def test_create_project_positive():
    api = YouGileAPI()

    company_id = api.get_company_id()
    assert company_id is not None

    auth_result = api.authenticate(company_id)
    assert auth_result == True

    resp = api.create_project("Новый проект")
    assert resp.status_code == 201
    print("Проект создан!")

# Негативный тест (создание проекта с невалидными данными)
def test_create_project_negative():
    api = YouGileAPI()

    company_id = api.get_company_id()
    assert company_id is not None

    auth_result = api.authenticate(company_id)
    assert auth_result == True

    resp = api.create_project("")
    assert resp.status_code in [400, 422]
    print("Ошибка: новый проект не создан, отсутствует title!")
