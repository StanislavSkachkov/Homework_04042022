from itertools import count
from math import factorial

def yield_func():
    for el in count(int(input("Введите число до 10: "))):
        if el > 10:
            print ("Введено некорректное число")
            break
        else:
            yield factorial(el)
i = 1
my_list = []
for el in yield_func():
    if i > 20:
        break
    else:
        my_list.append(el)
        i += 1
print (my_list)