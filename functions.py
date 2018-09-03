import json


# Loads lexicons
def load_word() -> dict:
    """
    Reads a dictionary from a json file.
    :return: Dict with words from a dictionary: {word: 1}
    """
    try:
        with open('lexicon.json', 'r', encoding='UTF-8') as lexicon_file:
            words = json.load(lexicon_file)
            return words
    except FileNotFoundError as e:
        print("Dictionary file not found.", e)
    except Exception as e:
        print(e)


# importing lexicons in json format
loaded_json_file = load_word()
positives = loaded_json_file['positive'].keys()
negatives = loaded_json_file['negative'].keys()
neutrals = loaded_json_file['neutral'].keys()


# searching for txt files in folder
def search_for_text():
    """
    Shows available files in .txt format in the current folder apart from lexicons
    A user has to select one of them
    The chosen text file is being processed in the next steps
    :return: string(text)
    """
    import os
    import fnmatch
    print('Found files:')
    list_of_files = os.listdir('.')
    pattern = "*.txt"
    excluded_files = ['negative-words.json', 'neutral-words.json', 'positive-words.txt']
    for entry in list_of_files:
        if fnmatch.fnmatch(entry, pattern):
            if entry not in excluded_files:
                print(entry)
    choosen_text = input('Which one do you what to work with?')
    if choosen_text in excluded_files:
        exit('Permission denied. Program closed.')
    return str(choosen_text)


# Nobody knows why its here, not in main file...
def show_text(argument):
    """
    Shows unformatted text
    :param argument: processing text -> str
    :return: str
    """
    print(argument, '\n' * 2)


def show_sent(argument):
    """
    Shows splitted text in sentences with numeration
    :param argument: processing text -> str
    :return: str
    """
    for index, sentence in enumerate(argument):
        if sentence[0].isupper() and (sentence[-1] == '.' or '?' or '!'):
            print(index, sentence)


# Checks character of words in text
def check_words_character(character, text):
    """
    Checks character of words in the text
    :param character: name of a lexicon -> str
    :param text: processing text -> str
    :return:
    """
    if character == 'positives':
        lexicon = positives
    elif character == 'negatives':
        lexicon = negatives
    else:
        return None
    i = [i for i in text if i in lexicon]
    return list(set(i))


def count_char_words(lexicon, text):
    """
    Counts words in the splitted text based on a chosen lexicon
    :param lexicon: str
    :param text: tuple str
    :return: int
    """
    number = 0
    for spam in text:
        if spam in check_words_character(lexicon, text):
            number += 1
    return number


# Counting unclassified words
def count_nochar(argument, number):
    pos = positives
    neg = negatives

    stop_words = ['-', ',', '(', ')']
    a = [a for a in argument if a.lower() not in pos and a.lower() not in neg and a.lower() not in stop_words]
    print(f'10 first unclassified words: {", ".join(list(set(a[:number])))}')
    z = 0
    for word in argument:
        if word not in pos:
            if word not in neg:
                z += 1
    return z


# Counting words in text
def count_words(argument):
    """
    Counts words in the splitted text
    :param argument: tuple str
    :return: int
    """
    return len(argument)


# Checks character of word
def check_char(word):
    if word in positives:
        return 'positive'
    elif word in negatives:
        return 'negative'
    elif word in neutrals:
        return 'neutral'
    else:
        return 'null'


# Check character of word and shows info about it
def show_char(word):
    word = word.lower()
    check = check_char(word)
    if check == 'positive':
        return f'The word <{word}> has a positive character.'
    elif check == 'negative':
        return f'The word {word} has a negative character.'
    elif check == 'neutral':
        return f'The word {word} has a neutral character.'
    elif check == 'null':
        return f'The word {word} is not found in any lexicon. \n ' \
               f'Would you like to add this word to a lexicon? => type "D"'
    else:
        return 'Unexpected error.'


###########################################################
# TO DO: Refactor function - use one json, not three of them
###########################################################

#  Adding word to suitable lexicon
def adding(word, leks):
    """
    Checks if the word exists in any lexicon, if not - adds it as a new record to a suitable json file
    :param word: str
    :param leks: str
    :return: str
    """
    new_word = {word: 1}
    if leks == 'positive':
        with open('positive-words.json') as load_positive_json:
            positive_data = json.load(load_positive_json)
        positive_data.update(new_word)
        with open('positive-words.json', 'w') as positive_json:
            json.dump(positive_data, positive_json)
        return f'The word <{word}> has been added to the positive words lexicon.'

    elif leks == 'negative':
        with open('negative-words.json') as load_negative_json:
            negative_data = json.load(load_negative_json)
        negative_data.update(new_word)
        with open('negative-words.json', 'w') as negative_json:
            json.dump(negative_data, negative_json)
        return f'The word <{word}> has been added to the negative words lexicon.'

    elif leks == 'neutral':
        with open('neutral-words.json') as load_neutral_json:
            neutral_data = json.load(load_neutral_json)
            neutral_data.update(new_word)
        with open('neutral-words.json', 'w') as neutral_json:
            json.dump(neutral_data, neutral_json)
        return f'The word <{word}> has been added to the neutral words lexicon.'

    else:
        return 'Unexpected error while adding word to the lexicon.'


# TO DO LATER
# def add_new_text(text, title):
#     """
#     Allows to add the new text to local library as txt for future analyze
#     :param text: str
#     :param title: str
#     :return: boolean
#     """


if __name__ == '__main__':
    pass
