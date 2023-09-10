from dirty_functions import random_famous
import os


def test_random_famous():
    # кол-во возвращаемых элементов списка
    FAMOUS = ('Max', 'Leo', 'Kate')
    assert len(random_famous(FAMOUS, 2)) == 2
    # что вернулось то что есть в исходом списке а не левые элементы
    for person in random_famous(FAMOUS, 2):
        assert person in FAMOUS

    # 2 элента тип строка данных тип строка
    # first_person = random_famous(FAMOUS, 2)[0]
    # assert isinstance(first_person, str)
    #
    # first_person = random_famous(({'Leo': 30}, {'Max': 41}, {'Kate': 32}), 2)[0]
    # assert isinstance(first_person, str)

    # Как проверить что они рандом ???
    result = []
    for i in range(800):
        person = random_famous(FAMOUS, 1)[0]
        result.append(person)

    assert len(set(result)) > 1


def test_mkdir():
    """Тест для функции с побочным эффектом"""
    os.mkdir('folder_mk')
    # папка есть на диске
    assert 'folder_mk' in os.listdir()

    os.rmdir('folder_mk')
