import random
Number_of_tries = 10

def choose_topic():
    topic = input('Выберите одну из трёх тем: 1 - блюда турецкой кухни, 2 - фамилии актеров, 3 - языки: ') # 1 2 или 3
    if topic == '1':
        file = 'Блюда турецкой кухни.txt'
    elif topic == '2':
        file = 'Фамилии актеров.txt'
    else:
        file = 'Языки.txt'
    return file


def open_file():
    file = choose_topic()
    with open(file, encoding = 'utf-8') as f:
        text = f.read().lower()
    text = text.split('\n')
    word = random.choice(text)
    return word


def proceed(word):
    unknown_word = ['_' for i in range(len(word))]
    print(' '.join(unknown_word))        #с помощию джойна убираем пробелы чтобы выглядело красиво и список превратился в строку
    return unknown_word


def letters(unknown_word, word):
    letter = input('Введите букву: ').lower()
    if letter in word:
        for i in range(len(word)):
            if letter == word[i]:
                unknown_word[i] = letter
        print('Поздравляем! Вы угадали букву ')
        print(' '.join(unknown_word))
    else:
        print('Вы  не угадали:( ')
        global Number_of_tries
        Number_of_tries -= 1
        print('Кол-во оставшихся попыток {} '.format(Number_of_tries))
    return(unknown_word)


def main():
    word = open_file()
    unknown_word = proceed(word) 
    letters(unknown_word, word)
main()
    

    
