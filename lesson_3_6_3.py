import time
import math

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import \
    presence_of_all_elements_located as elem_loc
from selenium.webdriver.support.expected_conditions import \
    element_to_be_clickable as elem_click

answer = ''


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(f"\nAnswer: {answer}")


@pytest.mark.parametrize('npart', (895, 896, 897, 898, 899, 903, 904, 905))
def test_message_correct(browser, npart):
    global answer
    lesson_url = f'https://stepik.org/lesson/236{npart}/step/1'
    wait = WebDriverWait(browser, 9)
    # идем на страницу урока
    browser.get(lesson_url)
    # ждем пока пропадет спиннер и вставка ответа
    result = str(math.log(int(time.time())))
    wait.until(elem_click((By.TAG_NAME, 'textarea'))).send_keys(result)
    # отправка решения
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    # ждем появления результата решения
    wait.until(elem_loc((By.CLASS_NAME, 'attempt-message_correct')))
    message = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
    if message != 'Correct!':
        answer += message
    assert message == 'Correct!', 'message not "Correct!"'
