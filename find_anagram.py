# 'abba' & 'baab' == true
# 'abba' & 'bbaa' == true
# 'abba' & 'abbba' == false
# 'abba' & 'abca' == false

# Write a function that will find all the anagrams of a word from a list.
# You will be given two inputs a word and an array with words.
# You should return an array of all the anagrams or an empty array if there are none.

# anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']
# anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']
# anagrams('laser', ['lazing', 'lazy',  'lacer']) => []





# def anagrams(word, words):
#     sorted_word = "".join(sorted(word))
#     anagrams = []
#
#     for w in words:
#         sorted_words = "".join(sorted(w))
#         if sorted_word == sorted_words:
#             anagrams.append(w)
#
#
#     return anagrams

# filter version
# def anagrams(word, words):
#     return filter(lambda x: sorted(word) == sorted(x), words)


# short version
def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]





print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))