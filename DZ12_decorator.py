"""
Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
Подсказка:
from datetime import datetime
time = datetime.now()
"""
from datetime import datetime
import random


def my_decorator(func):
    def wrapper():
        start_time = datetime.now()
        print('start_time: ', start_time)
        func()
        end_time = datetime.now()
        print('end_time: ', end_time)
        duration = end_time - start_time
        print('duration: ', duration)
        print('-' * 50)

    return wrapper


@my_decorator
def each_num():
    list_of_numbers = [3, 5, 6, 7, 10, 30, 25, 6, 7, 30, 30, 3, 3, 3, 3]
    result = {}
    for num in list_of_numbers:
        if result.get(num, None):
            result[num] += 1
        else:
            result[num] = 1
    print('That is the result')
    print(result)
    print('-' * 50)


@my_decorator
def guess_num(): #the right number is 10
    right_num = 10 #random.randint(0, 100)
    n = -1

    while n != right_num:
        n = input('Ввести с клавиатуры целое число от 0 до 100: ')
        if not n.isdigit():
            continue
        else:
            n = int(n)
            if n != right_num:
                print('Try again')
                continue
            else:
                print('Right!')
                break
    print('-' * 50)


each_num()
guess_num()
