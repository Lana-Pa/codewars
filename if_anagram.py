# Given 2 strings. Check if they are anagrams

import string

# delete all unnecessary punctuation and spaces btw words
def del_punctuation(str):
    punc = string.punctuation + " "
    return "".join(ch for ch in str if ch not in punc)


def if_anagram_use_sorted(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()
    str1_clean = del_punctuation(string1)
    str2_clean = del_punctuation(string2)

    return sorted(str1_clean) == sorted(str2_clean)


# using dictionary to count all characters in string
# then count all occurrences of each character

def if_anagram_use_dic(string1,string2):
    string1 = string1.lower()
    string2 = string2.lower()
    str1_clean = del_punctuation(string1)
    str2_clean = del_punctuation(string2)

    # edge case check
    if len(str1_clean) != len(str2_clean):
        return False

    count = dict()

    for ch in str1_clean:
        if ch not in count:
            count[ch] = 1
        else:
            count[ch] +=1
    print(count)

    for ch in str2_clean:
        if ch not in count:
            count[ch] = 1
        else:
            count[ch] -=1
    print(count)

    for keys in count:
        if count[keys] != 0:
            return False
        return True



string1 = 'Public, relations!'
string2 = 'Crap: built - on, lies?'

print(if_anagram_use_sorted(string1,string2))

print(if_anagram_use_dic(string1,string2))