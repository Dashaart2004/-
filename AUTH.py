from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class AUTH:
    def __init__(self, driver: WebDriver) -> None:
        self.__driver = driver
        self.__driver.get("https://ru.yougile.com/team/settings-account")


    @allure.step("Проходим авторизацию")
    def auth(self):
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[type='email']"))
        )
        self.__driver.find_element(By.CSS_SELECTOR, "[type='email']").send_keys("daraartunina881@gmail.com")
        self.__driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys("daryaartyuninaasdfg")
        self.__driver.find_element(By.CSS_SELECTOR, '[role="button"]').click()
        
    @allure.step('Проверка перехода в личный профиль')
    def element_is_present(self):
        WebDriverWait(self.__driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[class="user-avatar"]'))
        )
        try:
            self.__driver.find_element(By.CSS_SELECTOR, '[class="user-avatar"]')
            return True
        except:
            return False
    
