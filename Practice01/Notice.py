import nltk


def get_notice(title='Notice'):
    """Return the text contained in a txt file"""
    f = open(title + '.txt', 'r')
    return f.read()


def get_word(word):
    """Return the word according to the problem rules
    * The first letter is replaced by '#'
    * If the word ends with a vowel, the vowel is replaces by '#voc'
    * If the word ends with a consonant, the consonant is replaces by '#cons'"""
    vowels = {'a', 'e', 'i', 'o', 'u'}
    word = '#' + word[1:]
    if word[-1] in vowels:
        word = word[:len(word) - 1] + '#voc'
    else:
        word = word[:len(word) - 1] + '#cons'
    return word + ' '


notice = get_notice()
file = open('Result.txt', 'a')
for w in nltk.word_tokenize(notice):
    file.write(get_word(w))
file.write('\n')
