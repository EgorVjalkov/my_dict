from my_dict import dict
from random import choice
from errors import errors


#Сколько слов в словаре
def count_the_dict():
    return dict.__len__()


#Спроси у словаря
def answer_in_eng():
    a = input('What`s a word?\n')
    for i in dict:
        if a == i[0]:
            return i[1]
    return 'not found in dict'


#Тренинг. Вбей количество проверок. Выбери словарик
def test_myself_eng(checks, list=dict):
    limit = len(list)
    if checks > limit:
        checks = int(input(f'Enter a new count of checks, which <= {limit}:\n'))
    i = 0
    sum = 0
    limit = len(list)
#    errors = []
    while (i+1) <= checks and (i+1) <= limit:
        test = choice(list)
        print(f'\t{test[0]}')
        if test[1] == input('What does it mean?\n'):
            sum += 1
            print('\t\tcorrect!')
        else: 
            print('\t\twrong')
#            errors.append(test)
        i += 1
        list.remove(test)
    return f'Finished. {sum}/{i}, {round(sum / i * 100)}%' 



#def add_to_the_dict(word, meaning):
#    dict.append([word, meaning])
#    return dict

#print(answer_in_eng())
#print(count_the_dict())
#print(test_myself_eng(40))
#test = choice(dict)
