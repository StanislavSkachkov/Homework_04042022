first_day_result = 2 # результат первого дня
final_result = 3 # финальный результат
day = 1

while first_day_result < final_result:
    first_day_result = first_day_result + ((first_day_result / 100) * 10)
    day += 1
    print(f'{day}-й день: {first_day_result:.2f} км')
print(f'На {day} день спортсмен достиг результата - не менее {round (first_day_result)}')