# count all occurrences of given element in array

def count_all(el, arr):

    return len([x for x in arr if x == el])






print(count_all("alive",["lively", "alive", "harp", "sharp", "armstrong", "alive", "alive"]))