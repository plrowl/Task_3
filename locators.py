from selenium.webdriver.common.by import By


class MainPageLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']//following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']//following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти'] ")
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")
    RECOVER_LINK = (By.XPATH, "//a[@href='/forgot-password']")

class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']//following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']//following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']//following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".input__error") 
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")

class RecoveryPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")

class ProfilePageLocators:
    PROFILE_LINK = (By.XPATH, "//a[@href='/account/profile']")
    CONSTRUCT_BUTTON = (By.XPATH, "//li/a[@href='/']")
    LOGO_LINK = (By.XPATH, "//div/a[@href='/']")
    EXIT_BUTTON = (By.XPATH, "//button[text()='Выход']")

class BurgerIngredientLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class,'tab_tab_type_current')]//span")
