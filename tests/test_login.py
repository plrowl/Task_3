import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from config import TEST_USER
from urls import BASE_URL
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators, RecoveryPageLocators


@allure.feature("Авторизация")
class TestLogin:

    @allure.title("Вход по кнопке «Войти в аккаунт» на главной")
    def test_login_home_page_button(self, driver):
        with allure.step("Нажимаем «Войти в аккаунт» на главной странице"):
            driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
        with allure.step("Вводим email и пароль"):
            driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_USER['email'])
            driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_USER['password'])
            driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
            WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located(MainPageLocators.MAKE_ORDER_BUTTON)
            )
            assert driver.current_url == BASE_URL

    @allure.title("Вход через кнопку «Личный кабинет»")
    def test_login_personal_account(self, driver):
        with allure.step("Переходим по кнопке 'Личный кабинет'"):
            driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
            driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_USER['email'])
            driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_USER['password'])
            driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
            WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located(MainPageLocators.MAKE_ORDER_BUTTON)
            )
            assert driver.current_url == BASE_URL

    @allure.title("Вход через форму регистрации")
    def test_login_registration(self, driver):
        with allure.step("Открываем форму регистрации через 'Личный кабинет'"):
            driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
            driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
            driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
            driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_USER['email'])
            driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_USER['password'])
            driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
            WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located(MainPageLocators.MAKE_ORDER_BUTTON)
            )
            assert driver.current_url == BASE_URL

    @allure.title("Вход через форму восстановления пароля")
    def test_login_recovery(self, driver):
        with allure.step("Открываем форму восстановления пароля через 'Личный кабинет'"):
            driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
            driver.find_element(*LoginPageLocators.RECOVER_LINK).click()
            driver.find_element(*RecoveryPageLocators.LOGIN_LINK).click()
            driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_USER['email'])
            driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_USER['password'])
            driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
            WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located(MainPageLocators.MAKE_ORDER_BUTTON)
            )
            assert driver.current_url == BASE_URL
