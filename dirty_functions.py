import random


def random_famous(famous, count=2):
    """
    Недетерминированная функция
    :param famous: список людей
    :param count: количество
    :return: случайных людей
    """
    return random.sample(famous, count)



