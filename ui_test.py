from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import allure
from AUTH import AUTH
from MainPage import MainPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@allure.feature("Авторизация")
@allure.description("Выполняем авторизацию")
@allure.id(1)
@allure.severity("Blocker")
@allure.title("Проходим авторизацию")
def test_authorization(driver):
    auth = AUTH(driver)
    auth.auth()
    result = auth.element_is_present()
    assert result == True


@allure.feature("Создание задачи")
@allure.description("Создаем новую задачу на доске")
@allure.id(2)
@allure.severity("Blocker")
@allure.title('Создание новой задачи')
def test_make_new_task(driver):
    auth = AUTH(driver)
    auth.auth()
    main_page = MainPage(driver)
    main_page.go_to_my_company()
    main_page.open_project()
    main_page.add_task("My first task")
    result = main_page.get_new_task()
    assert result is None


@allure.feature("Имя Пользователя")
@allure.description("Меняем имя пользователя и сохраняем")
@allure.id(3)
@allure.severity("Blocker")
@allure.title('Проверка сохранения нового имени')
def test_change_user_name(driver):
    auth = AUTH(driver)
    auth.auth()
    main_page = MainPage(driver)
    main_page.new_name_of_user("Darya")
    result = main_page.get_user_name()
    expected_name = "Darya"
    assert result == expected_name


@allure.feature("Имя пользователя")
@allure.description("Ввод пробелов в поле 'Имя пользователя'")
@allure.id(4)
@allure.severity("Blocker")
@allure.title('Проверка появления ошибки при сохранении пустого имени')
def test_negative_change_user_name(driver):
    auth = AUTH(driver)
    auth.auth()
    main_page = MainPage(driver)
    main_page.new_name_of_user(" ")
    result = main_page.get_mistake()
    assert result == "Имя не задано"


@allure.feature("Поиск задачи")
@allure.description("Выполняем поиск задачи")
@allure.id(5)
@allure.severity("Blocker")
@allure.title('Проверка возможности поиска задачи')
def test_find_task(driver):
    auth = AUTH(driver)
    auth.auth()
    main_page = MainPage(driver)
    main_page.go_to_my_company()
    main_page.search_task("My first task")
    result = main_page.get_result()
    assert result == True
    

