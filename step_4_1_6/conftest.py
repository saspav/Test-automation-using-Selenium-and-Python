import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="en",
                     help="Choose language: ru, en, es, ...")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        language_opt = {'intl.accept_languages': user_language}
        options = Options()
        options.add_experimental_option('prefs', language_opt)
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        ff_profile = webdriver.FirefoxProfile()
        ff_profile.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=ff_profile)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
