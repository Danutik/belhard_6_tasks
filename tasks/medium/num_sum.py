"""
Написать рекурсивную функцию sum_of_numbers, которая будет вычислять сумму
цифр целого числа.

Можно пользоваться только функциями, операторами и условиями.
"""


def sum_of_numbers(num: int):
    if num == 0:
        return 0
    else:
        result = sum_of_numbers(num // 10)
        result += num % 10
    return result


print(sum_of_numbers(125))
