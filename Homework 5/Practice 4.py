eng_rus_dict = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
with open('text practice 4', 'r', encoding='utf-8') as f:
    with open ('text practice 4 rus', 'w', encoding='utf-8') as f2:
        for line in f:
            en, *num = line.split()
            ru = eng_rus_dict[en]
            f2.write(' '.join([ru] + num) + "\n")