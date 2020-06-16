# A pangram is a sentence that contains every single letter of the alphabet at least once.
# For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).
#
# Given a string, detect whether or not it is a pangram. Return True if it is,
# False if not. Ignore numbers and punctuation.

import string

# delete all unnecessary chars in string
# def is_pangram(s):
#     all = set(string.ascii_lowercase)
#     s = s.lower().replace(" ", "")
#     s = set(list(filter(lambda x: x not in string.punctuation and x not in string.digits, s)))
#
#
#     if s == all:
#         return True
#     else:
#         return False

#faster way
def is_pangram(s):

    s = s.lower()
    for char in string.ascii_lowercase:
        if char not in s:
            return False
    return True


pangram = "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"

print(is_pangram(pangram))