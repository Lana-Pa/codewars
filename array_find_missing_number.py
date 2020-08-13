# Consider an array of non-negative integers. A second array is formed by shuffling the
# elements of the first array and deleting a random element.
# Given 2 arrays, find which element is missing in second array
import collections as c

def find1(ar1,ar2):

    for el in ar1:
        if el not in ar2:
            return el
    return "Element not found"

# Linear time solution. We can use a hashtable and store the number of times
# each element appears in the second array. Then for each element in the first array
# we decrement its counter. Once hit an element with zero count that’s the missing element

def find2(ar1, ar2):

    # Using default dict to avoid key errors
    d = c.defaultdict(int)

    # Add a count for every instance in Array 2
    for num in ar2:
        d[num] += 1

    for num in ar1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1
    print(d)


# Linear time and constant space complexity:
# Initialize a variable to 0, then XOR every element in the
# first and second arrays with that variable. In the end, the value of the
# variable is the result, missing element in array2.

def find3(ar1, ar2):
    result = 0

    # Perform an XOR between the numbers in the arrays
    for num in ar1 + ar2:
        result ^= num
        print(result)


    return result


ar1 = [1,2,3,4,5,6,7]
ar2 = [2,6,1,4,3,7]

print(find3(ar1,ar2))