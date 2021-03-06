from my_dict import dict
from random import choice
from my_dict_commnd import command_dict_git
from my_errors import my_errors
from tails_dict import *

#Сколько слов в словаре
def count_the_dict(list=dict):
    return list.__len__()


#Спроси у словаря
def answer_the_dict(list=dict):
    a = input('What`s a word/command?\n')
    for i in list:
        if a == i[0]:
            return i[1:]
    return 'not found in dict'

list = [['word', 'слово', 'буква']]

#Тренинг. Вбей количество проверок. Выбери словарик
def test_myself_eng(checks, list=dict):
    i = 0
    sum = 0
    errors = []
    limit = len(list)
    # блок по проверке длины словаря
    if checks > limit: 
        print(f'Количество вопросов превышает объем словаря, будет изменено на {limit}.')
        checks = limit
    # блок по выбору индекса как начало теста
    else: 
        start = input('From begin or end? Or get index? \n')
        if start == 'begin' or start == '': list = list[:checks]
        elif start == 'end': list = list[-checks:]
        elif type(int(start)) == int: 
            if checks > len(list)-int(start): list = list[len(list)-checks:]
            else: list = list[int(start):int(start)+checks]
    # блок по подбору вопросов
    while (i+1) <= checks:
        test = choice(list)
        print(f'\t{test[0]}')
        a = input('What does it mean?\n')
        right_answer = 0
        # блок по проверке ответа среди значений
        for meaning in test[1:]:
            if a == meaning:
                sum += 1
                right_answer += 1
        # блок обратной связи
        if right_answer > 0: print('\t\tcorrect!')
        else:
            print('\t\twrong!')
            errors.append(test)
        i += 1
        list.remove(test)
    print(f'Finished. {sum}/{i}, {round(sum / i * 100)}%')
    return errors



#def add_to_the_dict(word, meaning):
#    dict.append([word, meaning])
#    return dict

#print(answer_the_dict())
#print(count_the_dict())
print(test_myself_eng(40, tails_dict_23_5))
#test = choice(dict)