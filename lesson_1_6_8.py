from selenium import webdriver

try:
    values = ('Ivan', 'Petrov', 'Smolensk', 'Russia')
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_xpath_form")
    [elem.send_keys(values[num]) for num, elem in
     enumerate(browser.find_elements_by_tag_name("input"))]
    browser.find_element_by_xpath('//button[text()="Submit"]').click()
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
finally:
    browser.quit()
