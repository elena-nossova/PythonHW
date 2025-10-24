from YouGileApi import YouGileAPI

# Позитивный тест (изменение проекта)
def test_update_project_positive():
    api = YouGileAPI()
    api.get_company_id()
    api.authenticate()

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

    if api.api_key:
        api.delete_key()

# Негативный тест (изменение несуществующего проекта)
def test_update_project_negative():
    api = YouGileAPI()
    api.get_company_id()
    api.authenticate()

    update_data = {"title": "Новое название"}
    resp = api.update_project("несуществующий-id-12345", update_data)

    assert resp.status_code == 404
    print("Ошибка: проект с таким ID не найден!")

    if api.api_key:
        api.delete_key()