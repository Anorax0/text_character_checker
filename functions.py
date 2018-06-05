# Wyszukiwuje pliki tekstowe w aktualnym katalogu
def search_for_text():
    import os, fnmatch, time
    print('Wykryto powyższe teksty w katalogu:')
    time.sleep(0.5)
    listOfFiles = os.listdir('.')
    pattern = "*.txt"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            print(entry)
    choosen_text = input('Który z tych tekstów chcesz wczytać?')
    return str(choosen_text)

# Wybieranie pliku tekstowego do dalszej obróbki
def choose_text():
    choosen_text = input('Który z powyższych plików tekstowych chcesz wybrać? [nazwa.txt] \n')
    if choosen_text == 'positive-words.txt' or choosen_text == 'negative-words.txt':
        exit('Błąd dostępu. Program zakończono.')
    return str(choosen_text)


# Wyświetla wczytany tekst z oryginalnym formatowaniem
def show_text(argument):
    print(argument, '\n' * 2)

# Dzieli wczytany tekst na zdania i je numeruje
def show_sent(argument):
    x = 1
    for sentence in argument:
        if sentence[0].isupper() and (sentence[-1] == '.' or '?' or '!'):
            print(x, sentence)
            x += 1

# Kolejne 4 funkcje sprawdzają jakie są negatywne i pozytywne słowa
# Oraz sprawdzają ich ilość
def check_positives(argument):
    l_file = open(r'positive-words.txt', 'r', encoding='UTF-8')
    f = l_file.read()
    lex = f.split()
    i = [i for i in argument if i in lex]
    i = list(set(i))
    return i

def check_negatives(argument):
    l_file = open(r'negative-words.txt', 'r', encoding='UTF-8')
    f = l_file.read()
    lex = f.split()
    i = [i for i in argument if i in lex]
    i = list(set(i))
    return i

def count_positives(argument):
    j = 0
    for spam in argument:
        if spam in check_positives(argument):
            j += 1
    return j

def count_negatives(argument):
    j = 0
    for spam in argument:
        if spam in check_negatives(argument):
            j += 1
    return j

# Liczy ilość słów niesklasyfikowanych w leksykonach
def count_nochar(argument):
    p_file = open(r'positive-words.txt', 'r', encoding='UTF-8')
    p = p_file.read()
    po = p.split()
    n_file = open(r'negative-words.txt', 'r', encoding='UTF-8')
    n = n_file.read()
    no = n.split()
    neu_file = open(r'negative-words.txt', 'r', encoding='UTF-8')
    neu = n_file.read()
    neut = n.split()

    a = [a for a in argument if a.lower() not in po and a.lower() not in no and a.lower() not in neut]
    print(f'10 pierwszych niesklasyfikowanych słów: {list(set(a[:10]))}')
    z = 0
    for word in argument:
        if word not in po:
            if word not in no:
                z += 1
    return z

# liczy ilość słów
def count_words(argument):
    z = 0
    for word in argument:
        z += 1
    return z

# Sprawdza w którym leksykonie jest dane słowo
def check_char(word):
    pos = open(r'positive-words.txt', 'r', encoding='UTF-8').read().split()
    neg = open(r'negative-words.txt', 'r', encoding='UTF-8').read().split()
    non = open(r'neutral-words.txt', 'r', encoding='UTF-8').read().split()
    if word in pos:
        return 'pos'
    elif word in neg:
        return 'neg'
    elif word in non:
        return 'non'
    else:
        return 'Error'

# Sprawdza charakter słowa i sprawa info, o charakterze
def show_char(word):
    word = word.lower()
    check = check_char(word)
    if check == 'pos':
        return f'Słowo {word} ma charakter pozytywny.'
    elif check == 'neg':
        return  f'Słowo {word} ma charakter negatywny.'
    elif check == 'non':
        return  f'Słowo {word} ma charakter neutralny.'
    elif check == 'Error':
        return f'Słowo {word} nie występuje w leksykonie. \n  Jeśli chcesz dodać słowo do leksykonu => wybierz "D"'
    else:
        return 'Wystąpił jakiś błąd.'

# Dodaje słowo do wybranego leksykonu
def adding(word, leks):
    word, leks = word.lower(), leks.lower()
    if leks == 'pos':
        file = open(r'positive-words.txt', 'a', encoding='UTF-8')
        file.write(f'\n{word}')
        return f'Słowo {word} zostało dodane do leksykonu słów pozytywnych.'
    elif leks == 'neg':
        file = open(r'negative-words.txt', 'a', encoding='UTF-8')
        file.write(f'\n{word}')
        return f'Słowo {word} zostało dodane do leksykonu słów negatywnych.'
    elif leks == 'non':
        file = open(r'neutral-words.txt', 'a', encoding='UTF-8')
        file.write(f'\n{word}')
        return f'Słowo {word} zostało dodane do leksykonu słów neutralnych.'