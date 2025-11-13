import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import TEST_USER
from generators import UserGenerator
from urls import BASE_URL
from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators


@allure.feature("Регистрация")
@allure.story("Форма регистрации пользователей")
class TestRegistration:

    @allure.title("Успешная регистрация нового пользователя")
    def test_success_registration(self, driver):
        valid_user = UserGenerator.generate_user()

        with allure.step("Открываем форму регистрации"):
            driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
            driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
            driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(valid_user["name"])
            driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(valid_user["email"])
            driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(valid_user["password"])
            driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        with allure.step("Авторизуемся после регистрации"):
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
            )
            driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(valid_user["email"])
            driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(valid_user["password"])
            driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        with allure.step("Проверяем, что открылась главная страница"):
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(MainPageLocators.MAKE_ORDER_BUTTON)
            )
            assert driver.current_url == BASE_URL

    @allure.title("Ошибка при регистрации с коротким паролем")
    def test_registration_invalid_password_error(self, driver):
        invalid_user = UserGenerator.generate_user(valid_password=False)

        with allure.step("Открываем форму регистрации"):
            driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
            driver.find_element(*LoginPageLocators.REGISTER_LINK).click()

        with allure.step("Вводим данные с коротким паролем"):
            driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(invalid_user["name"])
            driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(invalid_user["email"])
            driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(invalid_user["password"])
            driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        with allure.step("Проверяем сообщение об ошибке"):
            error_message = WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located(RegisterPageLocators.ERROR_MESSAGE)
            ).text
            assert error_message == "Некорректный пароль"

    @allure.title("Ошибка при регистрации с пустым полем имени (кнопка неактивна)")
    def test_registration_empty_name_error(self, driver):
        user = UserGenerator.generate_user()

        with allure.step("Открываем форму регистрации"):
            driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
            driver.find_element(*LoginPageLocators.REGISTER_LINK).click()

        with allure.step("Заполняем email и пароль, имя оставляем пустым"):
            driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys("")
            driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(user["email"])
            driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(user["password"])
            register_button = driver.find_element(*RegisterPageLocators.REGISTER_BUTTON)
            assert register_button.is_enabled(), "Должна быть ошибка при пустом поле email/валидация/или неактивная кнопка Зарегистрироваться. Если бы кнопка была бы неактивно, то можно было бы сделать assert not register_button.is_enabled()"

    @allure.title("Ошибка при регистрации с пустым полем email")
    def test_registration_empty_email_error(self, driver):
        user = UserGenerator.generate_user()

        with allure.step("Открываем форму регистрации"):
            driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
            driver.find_element(*LoginPageLocators.REGISTER_LINK).click()

        with allure.step("Заполняем имя и пароль, email оставляем пустым"):
            driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(user["name"])
            driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys("")
            driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(user["password"])

        with allure.step("Проверяем, что кнопка регистрации неактивна"):
            register_button = driver.find_element(*RegisterPageLocators.REGISTER_BUTTON)
            assert register_button.is_enabled(), "Должна быть ошибка при пустом поле email/валидация/или неактивная кнопка Зарегистрироваться. Если бы кнопка была бы неактивно, то можно было бы сделать assert not register_button.is_enabled()"

    @allure.title("Ошибка при регистрации уже существующего пользователя")
    def test_registration_existing_user_error(self, driver):
        user = TEST_USER
        with allure.step("Открываем форму регистрации"):
            driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT_BUTTON).click()
            driver.find_element(*LoginPageLocators.REGISTER_LINK).click()
            driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(user["name"])
            driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(user["email"])
            driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(user["password"])
            driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        with allure.step("Проверяем сообщение об ошибке"):
            error_message = WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located(RegisterPageLocators.ERROR_MESSAGE)
            ).text
            assert error_message == "Такой пользователь уже существует"
