from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure


class MainPage:
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver

    @allure.step('Переход на вкладку "Моя компания"')
    def go_to_my_company(self):
        WebDriverWait(self.__driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Моя компания']"))
        )
        self.__driver.find_element(By.XPATH, '//div[text()="Моя компания"]').click()

    @allure.step('Открытие проекта')
    def open_project(self):
        self.__driver.find_element(By.CSS_SELECTOR, '[title="Try"]').click()

    @allure.step('Добавление новой задачи в проект')
    def add_task(self, term: str):
        self.__driver.find_element(By.XPATH, '//span[text()="Добавить задачу"]').click()
        self.__driver.find_element(By.CSS_SELECTOR, '[data-test="board-task-input-name"]').send_keys(term, Keys.RETURN)

    @allure.step('Проверка поля "Введите название задачи')
    def get_new_task(self):
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-test="board-task-input-name"]'))
        )
        self.__driver.find_element(By.CSS_SELECTOR, '[data-test="board-task-input-name"]').text

    @allure.step('Добавление нового имени пользователя')
    def new_name_of_user(self, term: str):
        text = self.__driver.find_element(By.CSS_SELECTOR, '[placeholder="Отображаемое имя…"]')
        text.clear()
        text.send_keys(term, Keys.RETURN)

    @allure.step('Получение имени пользователя')
    def get_user_name(self):
        name = self.__driver.find_element(By.CSS_SELECTOR, '[placeholder="Отображаемое имя…"]').get_attribute("value")
        return name

    @allure.step('Получение сообщения об ошибке')
    def get_mistake(self):
        text = self.__driver.find_element(By.CSS_SELECTOR, '[class="text-error-old"]').text
        return text

    @allure.step('Ввод названия задачи для поиска')
    def search_task(self, term: str):
        self.__driver.find_element(By.CSS_SELECTOR, '[placeholder="Поиск по компании"]').send_keys(term)

    @allure.step('Получение результата о поиске задачи')
    def get_result(self):
        try:
            self.__driver.find_element(By.XPATH, '//div[text()="Результаты поиска"]')
            return True
        except:
            return False
