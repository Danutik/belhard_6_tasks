"""
Написать функцию triangular_sequence, которая принимает n и возвращает
последовательность следующего вида:

1
22
333
4444
55555
...

Например:

n = 3:
1
22
333

n = 6:
1
22
333
4444
55555
666666
"""


def triangular_sequence(num):
    if num == 0:
        return str("")
    elif num >= 1:
        return triangular_sequence(num - 1) + (str(num) * num) + "\n"


print(triangular_sequence(5))
