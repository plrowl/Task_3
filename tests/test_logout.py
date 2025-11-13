import allure
from config import TEST_USER
from urls import LOGIN_URL
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from locators import LoginPageLocators


@allure.feature("Личный кабинет")
@allure.story("Выход из аккаунта")
class TestLogout:

    @allure.title("Проверка выхода из личного кабинета по кнопке «Выйти»")
    def test_logout_personal_account(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        with allure.step("Открываем форму входа через Личный кабинет и авторизуемся под тестовым пользователем"):
            main_page.go_to_personal_account()
            login_page.login(TEST_USER["email"], TEST_USER["password"])
            main_page.wait_loaded()

        with allure.step("Переходим в личный кабинет"):
            profile_page.open_profile()

        with allure.step("Нажимаем кнопку «Выйти»"):
            profile_page.logout()

        with allure.step("Проверяем, что отобразилась форма входа"):
            login_page.find(LoginPageLocators.LOGIN_BUTTON, timeout=5)

        with allure.step("Проверяем, что произошёл переход на страницу входа"):
            assert driver.current_url == LOGIN_URL
