import time
import math
import pytest

# https://github.com/saspav/Test-automation-using-Selenium-and-Python/blob/main/stepik_addons.py
from stepik_addons import MakeTask


class TestStepik:
    @classmethod
    def setup_class(cls):
        """
        Метод класса создает экземпляр класса MakeTask,
        авторизуется на Степике.
        """
        cls.task = MakeTask()
        cls.task.auth_stepik()
        cls.task.answer = ''

    @classmethod
    def teardown_class(cls):
        """Метод класса полученный ответ после тестов отправляет на Степик
        и закрывает браузер.
        """
        print(f'\nAnswer: {cls.task.answer}')
        lesson_url = 'https://stepik.org/lesson/237240/step/3?unit=209628'
        _ = cls.task.send_answer(lesson_url, cls.task.answer)
        cls.task.browser.quit()

    @pytest.mark.parametrize('npart', (895, 896, 897, 898, 899, 903, 904, 905))
    def test_message_correct(cls, npart):
        lesson_url = f'https://stepik.org/lesson/236{npart}/step/1'
        # отправляем решение на урок Степика (загрузка решения была реализована
        # ранее в методе класса MakeTask.send_answer)
        message = cls.task.send_answer(lesson_url,
                                       str(math.log(int(time.time()))))
        # если результат не 'Correct!' - добавляем его к строке
        if message != 'Correct!':
            cls.task.answer += message
        assert message == 'Correct!', 'message not "Correct!"'
