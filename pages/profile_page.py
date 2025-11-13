import allure
from locators import ProfilePageLocators, MainPageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step("Открываем личный кабинет ")
    def open_profile(self):
        self.click(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        self.click(ProfilePageLocators.PROFILE_LINK)

    @allure.step("Нажимаем кнопку Конструктор в личном кабинете")
    def go_to_constructor(self):
        self.click(ProfilePageLocators.CONSTRUCT_BUTTON)

    @allure.step("Нажимаем на логотип Stellar Burgers")
    def click_logo(self):
        self.click(ProfilePageLocators.LOGO_LINK)

    @allure.step("Выходим из аккаунта")
    def logout(self):
        self.click(ProfilePageLocators.EXIT_BUTTON)
