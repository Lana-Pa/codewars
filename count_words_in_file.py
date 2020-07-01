# Write a program that returns the count of each word in the file
import re

def count_words(file):
    file = open(file, 'r')
    dic = {}

    for line in file:
        line.lower()
        re.sub(r'[.,:?!:;[{}]', '', line)
        words = line.split()
        for word in words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word]+= 1

    # print words and counts
    # for key in dic:
    #     print(key, dic[key])

    #sort by counts
    sorted_values = sorted([(value, key) for (key, value) in dic.items()], reverse=True)

    for val in sorted_values:
        print(val[1], val[0])


file = "words.txt"
print(count_words(file))
