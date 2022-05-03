# импорт библиотек
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

driver = webdriver.Chrome()
driver.get('https://stepik.org/catalog?auth=login')
# WebDriverWait указывает время ожидания в секундах
wait = WebDriverWait(driver, 99)
# css-селектор элемента который мы ждем
items_selector = '#ember15'
# Здесь мы ждем появления элемента item_selector,
# если в течение 99 секунд он не появится, произойдет исключение
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, items_selector)))
# сохранение Куки в файл
with open(os.path.join(BASE_DIR, 'user_chrome.pkl'), 'wb') as f:
    pickle.dump(driver.get_cookies(), f)
driver.quit()
