with open("File_practice_3", "r", encoding='utf-8') as f:
    names = []
    aver_income = 0
    num = 0
    min_income = 20000
    for line in f:
        num = num + 1
        name, income = (i for i in line.split())
        income = float(income)
        if income < min_income:
            names.append(name)
        aver_income += income
    aver_income /= num
print(*names)
print(aver_income)