incomming = int(input('Внесите значение выручки')) # запрос выручки
oper_cost = int(input('Внесите значение издержек'))
profit = incomming - oper_cost # расчет прибыли

if incomming > oper_cost:
    rent = profit / incomming * 100 # расчет рентабельности выручки
    employ = int(input('введите количество сотрудников'))
    profit_for_employ = profit // employ # расчет рентабельности выручки на одного сотрудника
    print (f'Рентабельность выручки составляет {rent}')
    print (f'Прибыль фирмы на 1 сотрудника составляет {profit_for_employ}')

else:
    print('Издержки больше прибыли')
