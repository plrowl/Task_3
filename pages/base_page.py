import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def current_url(self):
        return self.driver.current_url

    def find(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def finds(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        return self.driver.find_elements(*locator)

    def is_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def click(self, locator, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        return element

    def action_click(self, locator, timeout=5):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        ActionChains(self.driver).move_to_element(element).click().perform()
        return element

    def type(self, locator, text, timeout=5, clear=True):
        element = self.find(locator, timeout)
        if clear:
            element.clear()
        element.send_keys(text)
        return element

    def get_text(self, locator, timeout=5):
        return self.find(locator, timeout).text


    def open(self, url):
        with allure.step(f"Открываем страницу: {url}"):
            self.driver.get(url)