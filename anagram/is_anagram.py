def is_anagram(word1, word2):
    '''
    Solution to the anagram problem
    :param word1: first word
    :param word2: second word
    :return: if second word is a possible anagram of word 1 return True else return False
    '''
    import re
    word1_set = set((re.sub("([., '])", "", word1)).lower())
    print(word1_set)
    word2_set = set((re.sub("([., '])", "", word2)).lower())
    print(word2_set)
    if word1_set == word2_set:
        return True
    else:
        return False


print(is_anagram("tE. a", "ea t"))
