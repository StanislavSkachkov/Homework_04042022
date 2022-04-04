user_name = 'Станислав' # создание переменной
user_age = 30 # создание переменной

print(user_name) # вывод переменной на экран
print(user_age)

user_name_request = input('Введите Ваше имя.') # запрос у пользователя
user_age_request = int(input('Введите Ваш возраст'))

print (f'Добрый день, {user_name_request}') # вывод на экран
print(f'Вам {user_age_request} лет')
