def count_words(string):
    '''
    Takes an input string and returns the amount of times a unique word is placed in the string.
    :param string: input string
    :return: Returns a dict {unique_word : times_repeated}
    '''
    import re as reg
    output = {}
    print(string)
    string = reg.sub('!|,|\?|\.', '', string).lower().split(' ')
    print(string)
    for key in string:
        output[key] = 0
        for term in string:
            if key == term:
                output[key] += 1
    return output


print(count_words('Oh wha,,,,,t a day what a lovely day!'))
