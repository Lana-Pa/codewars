# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.

# Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

# Example

# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

def sort_array(source_array):
    s_ar = []
    for el in source_array:
        if el%2 != 0 and el != 0:
            s_ar.append(el)
            s_ar.sort()

    for i in range(len(source_array)):
        if source_array[i]%2 == 0:
            s_ar.insert(i, source_array[i])
    return s_ar




print(sort_array([5, 3, 2, 8, 1, 4]))
