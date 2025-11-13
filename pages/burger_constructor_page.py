import allure
from locators import BurgerIngredientLocators
from pages.base_page import BasePage


class BurgerConstructorPage(BasePage):

    @allure.step("Ждем пока появятся вкладки конструктора")
    def wait_loaded(self, timeout=5):
        self.find(BurgerIngredientLocators.BUNS_TAB, timeout=timeout)

    @allure.step("Открывываем вкладку Булки")
    def click_buns_tab(self):
        self.action_click(BurgerIngredientLocators.BUNS_TAB)
        self.find(BurgerIngredientLocators.BUNS_SECTION)

    @allure.step("Открываем вкладку 'Соусы'")
    def click_sauces_tab(self):
        self.action_click(BurgerIngredientLocators.SAUCES_TAB)
        self.find(BurgerIngredientLocators.SAUCES_SECTION)

    @allure.step("Открываем вкладку 'Начинки'")
    def click_fillings_tab(self):
        self.action_click(BurgerIngredientLocators.FILLINGS_TAB)
        self.find(BurgerIngredientLocators.FILLINGS_SECTION)

    def get_active_tab_text(self):
        return self.get_text(BurgerIngredientLocators.ACTIVE_TAB)