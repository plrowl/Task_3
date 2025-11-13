import allure
from config import TEST_USER
from pages.main_page import MainPage
from pages.login_page import LoginPage


@allure.feature("Авторизация")
class TestLogin:

    @allure.title("Вход по кнопке «Войти в аккаунт» на главной")
    def test_login_home_page_button(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)

        with allure.step("Нажимаем «Войти в аккаунт» на главной странице"):
            main_page.go_to_personal_account()

        with allure.step("Авторизуемся тестовым пользователем"):
            login_page.login(TEST_USER["email"], TEST_USER["password"])

        with allure.step("Проверяем, что открылась главная страница"):
            main_page.wait_loaded()
            assert main_page.is_opened()