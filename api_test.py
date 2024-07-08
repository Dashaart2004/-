from reqapi import ApiRequests
import allure
import pytest

api = ApiRequests("https://ru.yougile.com/api-v2")


@pytest.mark.api_test
@allure.id(1)
@allure.severity("Blocker")
@allure.title("Проходим авторизацию")
def test_auth():
    result = api.registration_form()
    assert result == 200


@pytest.mark.api_test
@allure.id(2)
@allure.severity("Blocker")
@allure.title("Создание проекта")
def test_create_project():
    result = api.create_project()
    assert result == 201


@pytest.mark.api_test
@allure.id(3)
@allure.severity("Blocker")
@allure.title("Создание доски")
def test_create_board():
    result = api.create_board()
    assert result == 201


@pytest.mark.api_test
@allure.id(4)
@allure.severity("Blocker")
@allure.title("Создание колонки")
def test_create_column():
    result = api.create_new_column()
    assert result == 201


@pytest.mark.api_test
@allure.id(5)
@allure.severity("Blocker")
@allure.title("Получение информации о доске")
def test_get_board():
    result = api.get_board()
    assert result == 200
