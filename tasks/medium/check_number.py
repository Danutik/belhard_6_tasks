"""
Написать рекурсивную функцию check_number, которая должна возвращать True,
если переданное ей число n является степенью двойки (1 тоже степень двойки) и
False, если нет

Нельзя пользоваться операцией возведения в степень
"""


def check_number(n):
    if n == 1:
        return True
    elif n % 2 == 1:
        return False
    elif n > 1:
        return check_number(n / 2)


if check_number(5) is True:
    print("Данное число является степенью 2")
else:
    print("Данное число НЕ является степенью 2")
