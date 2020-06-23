# Write a script to find all occurrences of particular element in an array.


def find_word(ar, word):
    count = 0
    for wd in ar:
        if wd == word:
            count += 1
    return count

ar = ['no', 'sample', 'sample', 'yes', 'sample']
word = 'sample'

print(find_word(ar, word))