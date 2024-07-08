from selenium import webdriver
import pytest
import allure
from auth import AuthPage
from main import MainPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.mark.ui_test
@allure.id(1)
@allure.severity("Blocker")
@allure.title("Проходим авторизацию")
def test_authorization(driver):
    auth = AuthPage(driver)
    auth.auth()
    result = auth.element_is_present()
    assert result == True


@pytest.mark.ui_test
@allure.id(2)
@allure.severity("Blocker")
@allure.title('Создание новой задачи')
def test_make_new_task(driver):
    auth = AuthPage(driver)
    auth.auth()
    main_page = MainPage(driver)
    main_page.go_to_my_company()
    main_page.open_project()
    main_page.add_task("My first task")
    result = main_page.get_new_task()
    assert result is None


@pytest.mark.ui_test
@allure.id(3)
@allure.severity("Blocker")
@allure.title('Проверка сохранения нового имени')
def test_change_user_name(driver):
    auth = AuthPage(driver)
    auth.auth()
    main_page = MainPage(driver)
    main_page.new_name_of_user("Darya")
    result = main_page.get_user_name()
    expected_name = "Darya"
    assert result == expected_name


@pytest.mark.ui_test
@allure.id(4)
@allure.severity("Blocker")
@allure.title('Проверка появления ошибки при сохранении пустого имени')
def test_negative_change_user_name(driver):
    auth = AuthPage(driver)
    auth.auth()
    main_page = MainPage(driver)
    main_page.new_name_of_user(" ")
    result = main_page.get_mistake()
    assert result == "Имя не задано"


@pytest.mark.ui_test
@allure.id(5)
@allure.severity("Blocker")
@allure.title('Проверка возможности поиска задачи')
def test_find_task(driver):
    auth = AuthPage(driver)
    auth.auth()
    main_page = MainPage(driver)
    main_page.go_to_my_company()
    main_page.search_task("My first task")
    result = main_page.get_result()
    assert result == True
