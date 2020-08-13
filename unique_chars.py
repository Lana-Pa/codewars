# Given a string, determine if it is comprised of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return false.

def uni_char(s):

    # edge cases
    s = s.lower()
    if len(s) == 0:
        return False

    if len(s) == 1:
        return True

    # built-in solution
    # if len(set(s)) == len(s):
    #     return True
    # return False

    #  my solution with dictionary
    # d = {}
    # for ch in s:
    #     if ch not in d:
    #         d[ch] = 1
    #     else:
    #         d[ch] += 1
    # print(d)
    #
    # for value in d.values():
    #     if value > 1:
    #         return False
    #     return True



    # solution with set
    chars = set()
    for let in s:
        if let in chars:
            return False
        else:
            chars.add(let)
    return True


st = 'abc'
print(uni_char(st))
