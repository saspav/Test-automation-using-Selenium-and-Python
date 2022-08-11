from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage

# LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.should_be_add_product_to_basket_button()


def test_guest_added_product_to_basket(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.user_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_after_add_product()
    page.should_be_message_content_of_basket()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, browser.current_url)
    page.basket_should_be_empty()
    page.basket_should_be_empty_text()
