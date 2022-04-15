# Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию. Элементы выведите в
# порядке их следования в исходном списке. Для выполнения задания обязательно используйте
# генератор.

number_elem =  [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 1]

unique_number = set()
repeated_number = set ()
for number in number_elem:
    if number in repeated_number:
        continue
    if number in unique_number:
        repeated_number.add(number)
        unique_number.discard(number)
        continue
    unique_number.add(number)
print(unique_number)

print([number for number in number_elem if number in unique_number])