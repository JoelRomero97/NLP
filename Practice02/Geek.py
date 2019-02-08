import wikipedia
import nltk


def set_alphabet():
    """Return a set containing the complete alphabet (including lower and upper case)"""
    return sorted(set(map(chr, range(65, 91))).union(set(map(chr, range(97, 123)))))


def get_page_content(title='Geek', include_title=False):
    """Return the content of a wikipedia article using 'wikipedia' library for python"""
    wikipedia.set_lang('es')
    try:
        if include_title:
            return wikipedia.page(title).title + '\n' + wikipedia.page(title).content
        else:
            return wikipedia.page(title).content
    except wikipedia.HTTPTimeoutError:
        return 'The page \'' + title + '\' could not load'
    except wikipedia.PageError:
        return 'The page \'' + title + '\' does not exist'


def write_file(body, title='Geek'):
    """Write a file with a certain title and certain body"""
    file = open(title + '.txt', 'w')
    file.write(body)
    file.close()


def get_tokens(tokens):
    """Return a list containing all the words in the wikipedia article"""
    valid_token = False
    result = []
    for token in tokens:
        for letter in token:
            if letter not in alphabet:
                valid_token = False
                break
            else:
                valid_token = True
        if valid_token:
            result.append(token)
    return result


alphabet = set_alphabet()
content = get_page_content(include_title=True)
write_file(content)
page_tokens = nltk.word_tokenize(content)
words = get_tokens(page_tokens)
print('Number of unique words: ' + str(len(set(words))))
print('Number of tokens: ' + str(len(words)))
