import allure
from locators import RegisterPageLocators
from pages.base_page import BasePage


class RegisterPage(BasePage):

    @allure.step("Вводим имя при регистрации")
    def set_name(self, name: str):
        self.type(RegisterPageLocators.NAME_INPUT, name)

    @allure.step("Вводим email при регистрации")
    def set_email(self, email: str):
        self.type(RegisterPageLocators.EMAIL_INPUT, email)

    @allure.step("Вводим пароль при регистрации")
    def set_password(self, password: str):
        self.type(RegisterPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажимаем кнопку Зарегистрироваться")
    def submit(self):
        self.click(RegisterPageLocators.REGISTER_BUTTON)

    @allure.step("Регистрируем нового пользователя")
    def register(self, name: str, email: str, password: str):
        self.set_name(name)
        self.set_email(email)
        self.set_password(password)
        self.submit()

    def get_error_message(self):
        return self.get_text(RegisterPageLocators.ERROR_MESSAGE, timeout=3)

    def is_register_button_enabled(self):
        return self.find(RegisterPageLocators.REGISTER_BUTTON).is_enabled()

    @allure.step("Переходим на форму логина со страницы регистрации")
    def go_to_login(self):
        self.click(RegisterPageLocators.LOGIN_LINK)