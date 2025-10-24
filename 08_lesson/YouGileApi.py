import requests

class YouGileAPI:

    def __init__(self):
        self.base_url = "https://ru.yougile.com/api-v2"
        self.login = "ХХХХ"
        self.password = "ХХХХ"
        self.company_id = None
        self.api_key = None

    def _check_auth(self):

        if not self.api_key:
            raise ValueError("Авторизируйтесь в системе!")

    def get_company_id(self):
        url = f"{self.base_url}/auth/companies"
        auth_data = {
            "login": self.login,
            "password": self.password
        }
        resp = requests.post(url, json=auth_data)
        if resp.status_code != 200:
            return False

        data = resp.json()
        self.company_id = data['content'][0]['id']
        return True

    def authenticate(self):
        if not self.company_id:
            return False

        auth_url = f"{self.base_url}/auth/keys/get"
        auth_data = {
            "login": self.login,
            "password": self.password,
            "companyId": self.company_id
        }

        resp = requests.post(auth_url, json=auth_data)
        if resp.status_code != 200:
            return False

        resp_data = resp.json()
        self.api_key = resp_data[0]['key']
        return True

    def get_projects(self, limit=50, offset=0, include_deleted=False):
        self._check_auth()

        url = f"{self.base_url}/projects"
        params = {
            "limit": limit,
            "offset": offset,
            "includeDeleted": str(include_deleted).lower()
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        return requests.get(url, params=params, headers=headers)

    def create_project(self, title, users=None):
        self._check_auth()
        project_data = {
            "title": title
        }
        if users:
            project_data["users"] = users

        url = f"{self.base_url}/projects"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        resp = requests.post(url, json=project_data, headers=headers)
        return resp

    def get_project_by_id(self, project_id):
        self._check_auth()

        url = f"{self.base_url}/projects/{project_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        return requests.get(url, headers=headers)

    def update_project(self, project_id, update_data):
        self._check_auth()

        url = f"{self.base_url}/projects/{project_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        return requests.put(url, json=update_data, headers=headers)

    def delete_key(self):
        if not self.api_key:
            return False

        url = f"{self.base_url}/auth/keys/delete"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        resp = requests.post(url, headers=headers)
        if resp.status_code != 200:
            return False

        self.api_key = None
        return True