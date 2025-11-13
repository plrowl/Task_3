import allure
from config import TEST_USER
from urls import PERSONAL_ACCOUNT_URL, BASE_URL
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


@allure.feature("Личный кабинет")
@allure.story("Навигация и переходы")
class TestPersonalAccount:

    @allure.title("Переход в личный кабинет по клику на кнопку «Личный кабинет»")
    def test_open_personal_account(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        with allure.step("Открываем форму входа и логинимся"):
            main_page.go_to_personal_account()
            login_page.login(TEST_USER["email"], TEST_USER["password"])
            main_page.wait_loaded()

        with allure.step("Переходим в личный кабинет"):
            profile_page.open_profile()

        with allure.step("Проверяем, что открылась страница профиля"):
            assert profile_page.current_url.startswith(PERSONAL_ACCOUNT_URL)

    @allure.title("Переход в Конструктор по кнопке в личном кабинете")
    def test_personal_account_constructor_button(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        with allure.step("Открываем форму входа и логинимся"):
            main_page.go_to_personal_account()
            login_page.login(TEST_USER["email"], TEST_USER["password"])
            main_page.wait_loaded()

        with allure.step("Переходим в личный кабинет"):
            profile_page.open_profile()

        with allure.step("Нажимаем кнопку 'Конструктор'"):
            profile_page.go_to_constructor()

        with allure.step("Проверяем, что открылась главная страница"):
            main_page.wait_loaded()
            assert main_page.current_url == BASE_URL

    @allure.title("Переход в Конструктор по клику на логотип Stellar Burgers")
    def test_personal_account_constructor_logo(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        profile_page = ProfilePage(driver)

        with allure.step("Открываем форму входа и логинимся"):
            main_page.go_to_personal_account()
            login_page.login(TEST_USER["email"], TEST_USER["password"])
            main_page.wait_loaded()

        with allure.step("Переходим в личный кабинет"):
            profile_page.open_profile()

        with allure.step("Кликаем по логотипу в личном кабинете"):
            profile_page.click_logo()

        with allure.step("Проверяем, что открылась главная страница"):
            main_page.wait_loaded()
            assert main_page.current_url == BASE_URL
