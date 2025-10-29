from YouGileApi import YouGileAPI

# Позитивный тест (изменение проекта)
def test_update_project_positive():
    api = YouGileAPI()

    company_id = api.get_company_id()
    assert company_id is not None

    auth_result = api.authenticate(company_id)
    assert auth_result == True

    create_resp = api.create_project("Проект для изменения")
    assert create_resp.status_code == 201

    project_id = create_resp.json()["id"]

    update_data = {
        "title": "Измененное название проекта",
        "deleted": False
    }
    update_resp = api.update_project(project_id, update_data)
    assert update_resp.status_code == 200

    resp_data = update_resp.json()
    assert "id" in resp_data
    assert resp_data["id"] == project_id

# Негативный тест (изменение несуществующего проекта)
def test_update_project_negative():
    api = YouGileAPI()

    company_id = api.get_company_id()
    assert company_id is not None

    auth_result = api.authenticate(company_id)
    assert auth_result == True

    update_data = {"title": "Новое название"}
    resp = api.update_project("несуществующий-id-12345", update_data)
    assert resp.status_code == 404
    print("Ошибка: проект с таким ID не найден!")
