from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    promo_code = ''

    def get_promo_code(self):
        parts = self.browser.current_url.split('?')
        for part in parts:
            if '=' in part:
                values = part.split('=')
                if values[0] == 'promo':
                    promo_code = values[1]
                    return promo_code
        return ''

    def get_product_info(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return product_name, product_price

    def should_be_add_product_to_basket_button(self):
        assert self.is_element_present(
            *ProductPageLocators.BASKET_LINK), "Button add to basket is not presented"

    def user_can_add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET_LINK).click()

    def should_be_message_after_add_product(self):
        # проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        assert self.is_element_present(*ProductPageLocators.MESSAGE_AFTER_ADD), "Message after add is not presented"
        # получаем текст элементов для проверки
        product_name, product_price = self.get_product_info()
        message_add = self.browser.find_element(*ProductPageLocators.MESSAGE_AFTER_ADD).text
        # Проверяем, что продукт добавился
        assert product_name in message_add, "No product name in the message"

    def should_be_message_content_of_basket(self):
        # проверяем, что товар присутствует на странице
        assert self.is_element_present(*ProductPageLocators.MESSAGE_CONTENT_BASKET), "Message content basket is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not present"
        # получаем текст элементов для проверки
        product_name, product_price = self.get_product_info()
        message_content_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_CONTENT_BASKET).text.split()[-1]
        # проверяем, что цена товара есть в сообщении о стоимости корзины
        assert product_price == message_content_basket, "No product price is not equal to the product cost"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared"