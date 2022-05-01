from my_dict import dict
from random import choice
#from my_errors import my_errors


#Сколько слов в словаре
def count_the_dict():
    return dict.__len__()


#Спроси у словаря
def answer_in_eng():
    a = input('What`s a word?\n')
    for i in dict:
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
        checks = int(input(f'Enter a new count of checks, which <= {limit}:\n'))
    # блок по подбору вопросов
    while (i+1) <= checks and (i+1) <= limit:
        test = choice(list)
        print(f'\t{test[0]}')
        a = input('What does it mean?\n')
        right_answer = 0
        # блок по проверке ответа
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

print(answer_in_eng())
#print(count_the_dict())
#print(test_myself_eng(2))
#test = choice(dict)
