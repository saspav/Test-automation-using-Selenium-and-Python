import unittest
from selenium import webdriver


class TestRegistered(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.success = "Congratulations! You have successfully registered!"

    def tearDown(self):
        self.browser.quit()

    def try_registered(self, link):
        self.browser.get(link)

        for rf in ('first', 'second', 'third'):
            xpath = f'//div[@class="first_block"]//input[contains(@class, "{rf}")]'
            self.browser.find_element_by_xpath(xpath).send_keys(f'text_{rf}_field')

        self.browser.find_element_by_css_selector('button.btn').click()

        return self.browser.find_element_by_tag_name("h1").text

    def test_registered(self):
        link = "https://suninjuly.github.io/registration1.html"
        self.assertEqual(self.success, self.try_registered(link))

    def test_not_registered(self):
        link = "https://suninjuly.github.io/registration2.html"
        self.assertEqual(self.success, self.try_registered(link))


if __name__ == "__main__":
    unittest.main()
