import pytest
from YouGileApi import YouGileAPI

# Позитивный тест (получение списка проектов)
def test_get_projects_positive():
    api = YouGileAPI()

    company_id = api.get_company_id()
    assert company_id is not None

    auth_result = api.authenticate(company_id)
    assert auth_result == True

    resp = api.get_projects(limit=5)
    assert resp.status_code == 200
    data = resp.json()
    assert "content" in data
    assert "paging" in data

# Негативный тест (Получение списка без авторизации)
def test_get_projects_without_auth():
    api = YouGileAPI()

    with pytest.raises(ValueError, match="Авторизируйтесь в системе!"):
        api.get_projects()

    print("Ошибка авторизации")
