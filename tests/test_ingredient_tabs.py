import pytest
import allure
from pages.burger_constructor_page import BurgerConstructorPage


@allure.feature("Конструктор бургера")
@allure.story("Прокрутка по вкладкам ингредиентов")
class TestIngredientsTabs:

    @allure.title("Проверка перехода по вкладкам ингредиентов: {expected_text}")
    @pytest.mark.parametrize("tab_method, expected_text", [
        ("click_buns_tab", "Булки"),
        ("click_sauces_tab", "Соусы"),
        ("click_fillings_tab", "Начинки"),
    ])
    def test_click_tabs_scrolls_to_sections(self, driver, tab_method, expected_text):
        constructor_page = BurgerConstructorPage(driver)

        with allure.step("Ждём загрузку вкладок конструктора"):
            constructor_page.wait_loaded(timeout=10)

        with allure.step(f"Кликаем по вкладке '{expected_text}'"):
            getattr(constructor_page, tab_method)()

        with allure.step("Проверяем, что вкладка активна"):
            active_text = constructor_page.get_active_tab_text()
            assert active_text == expected_text, (
                f"Ожидалась вкладка '{expected_text}', но активна '{active_text}'"
            )