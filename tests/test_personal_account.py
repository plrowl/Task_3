import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import TEST_USER
from urls import PERSONAL_ACCOUNT_URL, BASE_URL
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators


import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import TEST_USER
from urls import PERSONAL_ACCOUNT_URL, BASE_URL
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators


@allure.feature("Личный кабинет")
@allure.story("Навигация и переходы")
class TestPersonalAccount:

    @allure.title("Переход в личный кабинет по клику на кнопку «Личный кабинет»")
    def test_personal_account_button(self, driver):
        with allure.step("Открываем форму входа через «Личный кабинет»"):
            driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
            driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_USER['email'])
            driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_USER['password'])
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
            ).click()
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
            ).click()

        with allure.step("Проверяем, что мы на странице личного кабинета"):
            WebDriverWait(driver, 5).until(EC.url_contains("/account"))
            assert driver.current_url.startswith(PERSONAL_ACCOUNT_URL.rstrip("/"))


    @allure.title("Переход из личного кабинета в Конструктор через кнопку «Конструктор»")
    def test_personal_account_constructor_button(self, driver):
        with allure.step("Открываем форму входа и логинимся"):
            driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
            driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_USER['email'])
            driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_USER['password'])
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable(ProfilePageLocators.CONSTRUCT_BUTTON)).click()
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable(MainPageLocators.MAKE_ORDER_BUTTON))
            assert driver.current_url == BASE_URL

    @allure.title("Переход в Конструктор по клику на логотип Stellar Burgers")
    def test_personal_account_constructor_logo(self, driver):
        with allure.step("Открываем форму входа и логинимся"):
            driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
            driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_USER['email'])
            driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_USER['password'])
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)).click()
            WebDriverWait(driver, 3).until(EC.element_to_be_clickable(ProfilePageLocators.LOGO_LINK)).click()
            assert driver.current_url == BASE_URL
