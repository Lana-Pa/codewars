# You are given a word. Now, using your favorite programming language,
# write a code to test if the word that is given to you is a palindrome.
# [ Palindromes are words that have similar characters from left and right both. Ex: noon, radar, civic, etc.]

# with reversed method
# def palindrome(word):
#     if list(word) == list(reversed(word)):
#          return True
#     return False

# with slicing
def palindrome(word):
    if word == word[::-1]:
         return True
    return False



print(palindrome('civic'))