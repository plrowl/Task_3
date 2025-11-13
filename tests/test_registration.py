import allure
from config import TEST_USER
from generators import UserGenerator
from urls import BASE_URL
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from locators import LoginPageLocators

@allure.feature("Регистрация")
@allure.story("Форма регистрации пользователей")
class TestRegistration:

    @allure.title("Успешная регистрация нового пользователя")
    def test_success_registration(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        register_page = RegisterPage(driver)

        user = UserGenerator.generate_user(valid_password=True)

        with allure.step("Открываем форму регистрации"):
            main_page.go_to_personal_account()
            login_page.go_to_register()

        with allure.step("Заполняем форму регистрации валидными данными"):
            register_page.register(user["name"], user["email"], user["password"])

        with allure.step("Проверяем, что нас перекинуло на форму входа"):
            assert login_page.is_visible(LoginPageLocators.LOGIN_BUTTON)

    @allure.title("Ошибка при регистрации с коротким паролем")
    def test_registration_short_password(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        register_page = RegisterPage(driver)

        user = UserGenerator.generate_user(valid_password=False)

        with allure.step("Открываем форму регистрации"):
            main_page.go_to_personal_account()
            login_page.go_to_register()

        with allure.step("Пытаемся зарегистрироваться с коротким паролем"):
            register_page.register(user["name"], user["email"], user["password"])

        with allure.step("Проверяем сообщение об ошибке"):
            error_message = register_page.get_error_message()
            assert error_message == "Некорректный пароль"

    @allure.title("Ошибка при регистрации уже существующего пользователя")
    def test_registration_existing_user(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        register_page = RegisterPage(driver)

        user = TEST_USER

        with allure.step("Открываем форму регистрации"):
            main_page.go_to_personal_account()
            login_page.go_to_register()

        with allure.step("Пытаемся зарегистрировать уже существующего пользователя"):
            register_page.register(user["name"], user["email"], user["password"])

        with allure.step("Проверяем сообщение об ошибке"):
            error_message = register_page.get_error_message()
            assert error_message == "Такой пользователь уже существует"
