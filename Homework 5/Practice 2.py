with open("Practice 2 text", "r", encoding='utf-8') as f:
    my_line = f.readlines ()
    for index, value in enumerate(my_line,1):
        word_amount = len(value.split())
        print(f"Строка {index} имеет {word_amount} слов")
