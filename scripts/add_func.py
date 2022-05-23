def add_new():
    english_word = input('a word: ')
    meaning1 = input('a first meaning: ')
    meaning2 = input('a second meaning: ')
    meaning3 = input('a thrid meaning: ')
    new_word_list = [english_word, meaning1]
    if meaning2 == '': return f"{new_word_list}, "
    elif meaning2 != '' and meaning3 == '': 
        new_word_list.append(meaning2)
        return f"{new_word_list}, "
    else: 
        new_word_list.append(meaning2)
        new_word_list.append(meaning3)
        return (f"{new_word_list}, ")

def print_a_new():
    print(add_new())

#write_new()
#print(add_new())