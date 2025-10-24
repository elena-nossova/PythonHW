import pytest
from YouGileApi import YouGileAPI

def test_full_auth_with_cleanup():
    api = YouGileAPI()

    assert api.get_company_id() == True
    assert api.authenticate() == True

    resp = api.get_projects(limit=5)
    assert resp.status_code == 200
    data = resp.json()
    assert "content" in data
    assert "paging" in data

    if api.api_key:
        api.delete_key()

# Негативный тест (Получение списка без авторизации)
def test_get_projects_without_auth():
    api = YouGileAPI()

    with pytest.raises(ValueError, match="Авторизируйтесь в системе!"):
        api.get_projects()

# Позитивный тест (создание проекта)
def test_create_project_positive():
    api = YouGileAPI()
    api.get_company_id()
    api.authenticate()

    resp = api.create_project("Новый проект")
    assert resp.status_code == 201
    print("Проект создан!")

    if api.api_key:
        api.delete_key()

# Негативный тест (создание проекта с невалидными данными)
def test_create_project_negative():
    api = YouGileAPI()
    api.get_company_id()
    api.authenticate()

    resp = api.create_project("")
    assert resp.status_code in [400, 422]
    print("Ошибка: новый проект не создан, отсутствует title!")

    if api.api_key:
        api.delete_key()