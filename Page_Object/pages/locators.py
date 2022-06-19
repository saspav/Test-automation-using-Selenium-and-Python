from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.NAME, "login_submit")
    REGISTER_FORM = (By.NAME, "registration_submit")


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".price_color")
    BASKET_LINK = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_AFTER_ADD = (By.CSS_SELECTOR, "div.alertinner")
    MESSAGE_CONTENT_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner")
