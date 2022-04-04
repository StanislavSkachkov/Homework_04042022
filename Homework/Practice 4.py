x = int(input ("Введите целое положительное число")) # запрос числа
y = -1

while x > 10:
    z = x % 10
    x //= 10
    if z > y:
        y = z
print(y)
