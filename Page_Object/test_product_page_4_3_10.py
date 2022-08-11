from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    page = BasketPage(browser, browser.current_url)
    page.basket_should_be_empty()
    page.basket_should_be_empty_text()
