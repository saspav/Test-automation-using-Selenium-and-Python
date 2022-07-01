import pytest
from .pages.product_page import ProductPage

LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

# первичная проверка
urls = [f"{LINK}?promo=offer{num}" for num in range(10)]

# отметка упавшего теста
fail = 7
failed = pytest.param(f"{LINK}?promo=offer{fail}",
                      marks=pytest.mark.xfail(reason="bag on page"))
urls = [f"{LINK}?promo=offer{num}" if num != fail else failed
        for num in range(10)]


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.user_can_add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_after_add_product()
    page.should_be_message_content_of_basket()
