import pytest


# область покрытия class означает, что фикстура будет вызываться один раз
# для класса
@pytest.fixture(scope="class")
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")  # эта часть выполнится только после прогона всех тестов


@pytest.fixture()
def very_important_fixture():
    print(":)", "\n")


# параметр autouse=True указывает на то, что данная фикстура будет
# запускаться для каждого теста, даже без явного вызова
@pytest.fixture(autouse=True)
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():
    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        # вызываем фикстуру prepare_faces в тесте, передав ее как параметр
        # (выполнится сначала "^_^",
        # а потом после окончания второго теста ":3")
        # вызываем фикстуру very_important_fixture, передав ее как параметр
        # не передаём как параметр фикстуру print_smiling_faces,
        # но она все равно выполняется
        pass

    def test_second_smiling_faces(self, prepare_faces):
        # фикстура prepare_faces вызывается в данном тесте, но так как она
        # задана для класса, то тут выполняться не будет
        # не передаём как параметр фикстуру print_smiling_faces,
        # но она все равно выполняется
        pass
