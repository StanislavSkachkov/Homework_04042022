# Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументо

def my_func (el_1, el_2, el_3):
    my_func_list = [el_1, el_2, el_3]
    result_list = []
    result_list.append(max(my_func_list))
    my_func_list.remove(max(my_func_list))
    result_list.append(max(my_func_list))
    print (sum (result_list))


my_func(10, 15, 20)
