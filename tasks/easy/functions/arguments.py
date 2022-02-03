"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.

Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").
Проверить, что все аргументы целые можно с помощью функции all:
https://pyneng.readthedocs.io/ru/latest/book/10_useful_functions/all_any.html

Если все аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").

Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""


def dict_from_args(*args, **kwargs):
    if not all(isinstance(i, int) for i in args):
        raise TypeError("Все позиционные аргументы должны быть целыми")
    else:
        args_sum = sum(args)
    for key, value in kwargs.items():
        if type(key) and type(value) != str:
            raise TypeError("Все аргументы - ключевые слова должны быть строками")
        else:
            kwargs_max_len = max(len(k) and len(v) for k, v in kwargs.items())
        result = {"args_sum": args_sum, "kwargs_max_len": kwargs_max_len}

        return result
