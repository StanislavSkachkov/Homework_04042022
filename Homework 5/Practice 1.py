# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка

first_open = open("new_text_file_Practice_1.txt", "w", encoding='utf-8')
user_data = input ("Введите информацию. Если хотите выйти, оставьте пустую строку\n")
first_open.writelines(user_data)
while user_data:
    user_data = input("Введите текст: \n")
    first_open.writelines(user_data)
    if not user_data:
        break
first_open.close()

first_open = open("new_text_file_Practice_1.txt", "r", encoding='utf-8')
read_line = first_open.read().splitlines()
print (read_line)
first_open.close()
