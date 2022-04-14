# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и
# возвращающую их же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def upper_func(word):
    return word[0].upper() + word[1:].lower()


question = input("Введите слово: ").split()
for el, word in enumerate(question):
    if not word.isalpha() or not word.islower() or not word.isascii():
        print ("введите маленькие латинские буквы")
    else:
        question[el]= upper_func(word)
print (''.join(question))
