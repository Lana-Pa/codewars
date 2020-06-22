# Given two arrays of strings a1 and a2 return a sorted array r in lexicographical
# order of the strings of a1 which are substrings of strings of a2.

# #Example 1: a1 = ["arp", "live", "strong"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# returns ["arp", "live", "strong"]

# #Example 2: a1 = ["tarp", "mice", "bull"]
# a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
# returns []
# Notes:
# Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
# Beware: r must be without duplicates.
# Don't mutate the inputs.


# def in_array(array1, array2):
#     r = []
#     for string1 in array1:
#         for string2 in array2:
#             if string1 in string2:
#                 if string1 not in r:
#                     r.append(string1)
#                     r.sort()
#     return r



# short
def in_array(a1, a2):
    return sorted(set(s1 for s1 in a1 if any(s1 in s2 for s2 in a2)))





a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']
print(in_array(a1, a2))