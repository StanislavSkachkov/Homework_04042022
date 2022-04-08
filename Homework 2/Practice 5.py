first_list = [7, 9, 5, 4, 3, 6]
new_list = sorted(first_list)
revers_list = list(reversed(new_list))
print (revers_list)

request_ammout = 5
i = 1
while i < request_ammout:
    for el in range(len(revers_list)):
        num_question = int(input('Введите натуральное число: '))
        if revers_list[el] == num_question:
            revers_list.insert(el + 1, num_question)
            break
        elif revers_list[0] < num_question:
            revers_list.insert(0, num_question)
        elif revers_list[-1] > num_question:
            revers_list.append (num_question)
        elif revers_list[el] > num_question:
            revers_list.insert(el + 1, num_question)
        print (f'текущий список - {revers_list}')
        num_question = int(input('Введите натуральное число: '))
    i += 1
