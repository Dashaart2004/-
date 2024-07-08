import requests
import allure


class ApiRequests:

    def __init__(self, url):
        self.url = url

    @allure.step("Авторизаия")
    def registration_form(self):
        headers = {
           'Content-Type': 'application/json'
        }
        creds = {
            "login": "daraartunina881@gmail.com",
            "password": "daryaartyuninaasdfg",
            "name": "Поток_68.2"
        }
        resp = requests.post(self.url+'/auth/companies', headers=headers, json=creds)
        return resp.status_code

    @allure.step("Создание проекта")
    def create_project(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer iWnE-M1QH1HPjcF-fgILMYJc93sUAQ5mwR9seMn0DZNKCtUrGIPb-vnNN3dHthz+'
        }
        creds = {
            "title": "My first project diploma",
            "users": {"c7ed13cb-2c2c-4006-9ef4-849544cd2dcf": "admin"}
        }
        resp = requests.post(self.url + '/projects', headers=headers, json=creds)
        return resp.status_code

    @allure.step("Создание доски")
    def create_board(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer iWnE-M1QH1HPjcF-fgILMYJc93sUAQ5mwR9seMn0DZNKCtUrGIPb-vnNN3dHthz+'
        }
        data = {
            "title": "New board",
            "projectId": "0d4cb9e2-e730-4e9d-8eb9-78fe306d4746",
            "stickers": {
            "timer": False,
            "deadline": True,
            "stopwatch": True,
            "timeTracking": True,
            "assignee": True,
            "repeat": True,
            "custom": {
            "fbc30a9b-42d0-4cf7-80c0-31fb048346f9": False,
            "645250ca-1ae8-4514-914d-c070351dd905": False
        }
         }
        }
        resp = requests.post(self.url + '/boards', headers=headers, json=data)
        return resp.status_code

    @allure.step("Создание колонки")
    def create_new_column(self):
        data = {
            "title": "Новая колонка 1",
            "color": 2,
            "boardId": "2002fd76-4797-4720-aa83-311f08c0bc12"
        }
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer iWnE-M1QH1HPjcF-fgILMYJc93sUAQ5mwR9seMn0DZNKCtUrGIPb-vnNN3dHthz+'
        }
        resp = requests.post(self.url + '/columns', headers=headers, json=data)
        return resp.status_code

    @allure.step("Получение информации о доски")
    def get_board(self):
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer iWnE-M1QH1HPjcF-fgILMYJc93sUAQ5mwR9seMn0DZNKCtUrGIPb-vnNN3dHthz+'
        }
        board_id = "2002fd76-4797-4720-aa83-311f08c0bc12"
        resp = requests.get(self.url + '/boards/' + board_id, headers=headers)
        return resp.status_code
