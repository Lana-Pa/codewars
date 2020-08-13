# Given a string of words. Reverse all words. Delete expra spaces.

def reverse_words1(s):
    new_s = s.split()
    rev_str = new_s[::-1]
    return " ".join(rev_str)


def reverse_words2(s):
    return " ".join(reversed(s.split()))



s = " Hello John, how are you?  "

print(reverse_words2(s))