"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*data):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in data]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(data):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """


def is_prime(nums):
    list_prime = []
    for num in nums:
        k = 2
        if k == num:
            list_prime.append(num)
        elif num == 1:
            continue
        while num % k != 0:
            k += 1
            if k == num:
                list_prime.append(num)
    return list_prime


def filter_numbers(data, flag):
    if flag == "odd":
        return [number for number in data if number % 2 != 0]
    elif flag == "even":
        return [number for number in data if number % 2 == 0]
    elif flag == "prime":
        return is_prime(data)
