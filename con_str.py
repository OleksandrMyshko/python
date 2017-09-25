word = 'aabbb'
dictionary = ['aa', 'aab', 'bb']


def fun(word, dictionary):
    if word == '':
        return True
    for i in range(1, len(word) + 1):
        if (word[0:i] in dictionary and fun(word[i:], dictionary)):
            return True
    return False


print(fun(word, dictionary))
