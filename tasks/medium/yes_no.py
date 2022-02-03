"""
Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет
"""


def yes_or_no(some_list: list):
    before = set()
    for i in some_list:
        if i in before:
            print('Yes')
        else:
            print('No')
            before.add(i)


yes_or_no([1, 2, 3, 2, 5, 6, 1, 7])
