from itertools import count, cycle

def count_func():
    for el in count(int(input("Введите число: "))):
        if el > 100:
            break
        else:
            print (el)


def cycle_func():
    round_number = 0
    for el in cycle(input("Введите список элементов: ")):
        if round_number > 10:
            break
        else:
            print(el)
            round_number += 1
