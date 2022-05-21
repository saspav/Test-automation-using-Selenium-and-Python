link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_basket(browser):
    browser.implicitly_wait(9)
    browser.get(link)
    buttons = browser.find_elements_by_css_selector('.btn-add-to-basket')
    assert len(buttons), 'No button "Add to basket"!'
