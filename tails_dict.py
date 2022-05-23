tails_dict_23_5 = [

['deaf', 'глухой'], 
['probably', 'вероятно'], 
['affectionate', 'привязанный'], 
['to afraid', 'бояться'], 
['to pretend', 'претендовать', 'притворяться'], 
['splendid', 'великолепный'], 
['to fold', 'складывать', 'сгибать'],
['queer', 'странный'],
['patter', 'легкий топот'],
['neat', 'аккуратный', 'чистый'], 
['to trail', 'тащить', 'плестись', 'идти по следу'],
['rather', 'скорее', 'довольно'],
['beard', 'борода'], 
['several', 'некоторый', 'несколько'], 
['to exclaime', 'восклицать'], 
['inquisitive', 'пытливый'], 
['to delight', 'наслаждаться', 'восхищаться'], 
['to intend', 'намереваться', 'предназначать', 'иметь ввиду'], 
['to reign', 'царствовать', 'господствовать'],

]

def add_new(english_word, meaning1, meaning2='', meaning3=''):
    new_word_list = [english_word, meaning1]
    if meaning2 == '': return f"{new_word_list}, "
    elif meaning2 != '' and meaning3 == '': 
        new_word_list.append(meaning2)
        return f"{new_word_list}, "
    else: 
        new_word_list.append(meaning2)
        new_word_list.append(meaning3)
        return f"{new_word_list}, "

print(add_new('', '', '', ''))