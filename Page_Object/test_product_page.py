from .pages.product_page import ProductPage

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
