import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import TEST_USER
from urls import LOGIN_URL
from locators import MainPageLocators, LoginPageLocators, ProfilePageLocators


@allure.feature("Личный кабинет")
@allure.story("Выход из аккаунта")
class TestLogout:

    @allure.title("Проверка выхода из личного кабинета по кнопке «Выйти»")
    def test_logout_personal_account(self, driver):
        with allure.step("Открываем форму входа через «Личный кабинет»"):
            driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()

        with allure.step("Авторизуемся под тестовым пользователем"):
            driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_USER['email'])
            driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_USER['password'])
            driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        with allure.step("Ожидаем загрузку и открываем личный кабинет"):
            WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
            ).click()

        with allure.step("Нажимаем кнопку «Выйти»"):
            WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located(ProfilePageLocators.EXIT_BUTTON)
            ).click()

        with allure.step("Проверяем, что отобразилась форма входа"):
            WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
            )

        with allure.step("Проверяем, что произошёл переход на страницу входа"):
            assert driver.current_url == LOGIN_URL
