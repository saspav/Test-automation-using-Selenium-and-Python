# Полная автоматизация :)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import \
    text_to_be_present_in_element as text_in
from stepik_addons import MakeTask


class NewTask(MakeTask):
    def get_answer(self, task_url):
        """
        Получаем решение
        :param task_url: ссылка на задание
        :return: результат
        """
        self.browser.get(task_url)

        # ставим ожидание цены
        WebDriverWait(self.browser, 12).until(text_in((By.ID, 'price'),
                                                      '$100'))
        # кликаем на кнопку
        # browser.find_element_by_xpath('//button[text()="Book"]').click()
        self.browser.find_element_by_id('book').click()
        # ищем число
        x = self.browser.find_element_by_css_selector('#input_value').text
        print(x, self.calc(x))
        # втыкаем ответ
        self.browser.find_element_by_id('answer').send_keys(self.calc(x))
        # жмем сабмит
        # browser.find_element_by_xpath('//button[text()="Submit"]').click()
        self.browser.find_element_by_id('solve').click()
        # смотрим всплывающее окно и берем из него результат
        alert = self.browser.switch_to.alert
        self.result = alert.text.split()[-1]
        # без этого не работает дальнейший переход на степик
        alert.accept()
        return self.result


task = NewTask()
task.task_url = 'https://suninjuly.github.io/explicit_wait2.html'
task.lesson_url = 'https://stepik.org/lesson/181384/step/8?unit=156009'
task.solution()
