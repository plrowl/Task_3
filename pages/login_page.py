import allure
from locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Вводим email пользователя")
    def set_email(self, email: str):
        self.type(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step("Вводим пароль пользователя")
    def set_password(self, password: str):
        self.type(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажимаем кнопку Войти")
    def submit(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Авторизация")
    def login(self, email: str, password: str):
        self.set_email(email)
        self.set_password(password)
        self.submit()

    @allure.step("Переходим на страницу регистрации")
    def go_to_register(self):
        self.click(LoginPageLocators.REGISTER_LINK)

    @allure.step("Переходим на страницу восстановления пароля")
    def go_to_recovery(self):
        self.click(LoginPageLocators.RECOVER_LINK)