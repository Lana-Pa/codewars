# Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic
# characters and numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.
#
# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice

# def duplicate_count(text):
#     text_low = text.lower()
#     dups = {}
#     count = 0
#
#     for char in text_low:
#         if char in dups:
#             dups[char] += 1
#         else:
#             dups[char] = 1
#
#     for key, value in dups.items():
#         if value > 1:
#             count += 1
#
#     print(count)

# list comprehension
def duplicate_count(s):
    return len([c for c in set(s.lower()) if s.lower().count(c) > 1])


duplicate_count("indivisibility")

