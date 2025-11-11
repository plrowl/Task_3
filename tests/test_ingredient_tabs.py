import pytest
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import BurgerIngredientLocators


@allure.feature("Конструктор бургера")
@allure.story("Прокрутка по вкладкам ингредиентов")
class TestIngredientsTabs:

    @allure.title("Проверка перехода по вкладкам ингредиентов: {expected_text}")
    @pytest.mark.parametrize("tab_locator, section_locator, expected_text", [
        (BurgerIngredientLocators.BUNS_TAB, BurgerIngredientLocators.BUNS_SECTION, "Булки"),
        (BurgerIngredientLocators.SAUCES_TAB, BurgerIngredientLocators.SAUCES_SECTION, "Соусы"),
        (BurgerIngredientLocators.FILLINGS_TAB, BurgerIngredientLocators.FILLINGS_SECTION, "Начинки")
    ])
    def test_click_tabs_scrolls_to_sections(self, driver, tab_locator, section_locator, expected_text):
        with allure.step(f"Ожидаем, что вкладка '{expected_text}' кликабельна"):
            element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(tab_locator))
            ActionChains(driver).move_to_element(element).click().perform()
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located(section_locator))

        with allure.step("Проверяем, что вкладка активна"):
            active_text = driver.find_element(*BurgerIngredientLocators.ACTIVE_TAB).text
            assert active_text == expected_text, f"Ожидалась вкладка '{expected_text}', но активна '{active_text}'"
