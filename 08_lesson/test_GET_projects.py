import pytest
from YouGileApi import YouGileAPI

# Позитивный тест (получение списка)
def test_full_authentication_with_cleanup():
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

    print("Ошибка авторизации")