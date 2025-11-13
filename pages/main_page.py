import allure
from urls import BASE_URL
from locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Открываем главную страницу")
    def open_main(self):
        self.open(BASE_URL)

    @allure.step("Переходим в ЛК")
    def go_to_personal_account(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step("Нажимаем кнопку Войти в аккаунт на главной")
    def click_login_to_account(self):
        self.click(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)

    def wait_loaded(self):
        self.find(MainPageLocators.MAKE_ORDER_BUTTON)

    def is_opened(self):
        return self.current_url == BASE_URL