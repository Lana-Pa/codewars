# Given an integer array, output all the unique pairs that
# sum up to a specific value k.
#  output (1,4) and (2,3)
# for testing purposes change your function so it outputs a number of pairs

# solution #1
# def unique_pairs(lst, k):
#    if len(arr) < 2:
#         return
#
#     lst = list(set(lst))
#     pair = tuple()
#     count = 0
#
#
#     for i in lst:
#
#         diff = k - i
#         if diff in lst:
#             pair = i, diff
#             lst = lst[i+1:]
#             print(pair)
#             count += 1
#     return count
#
# The O(N) algorithm uses the set data structure. We perform a linear pass from the beginning and
# for each element we check whether k-element is in the set of seen numbers. If it is, then we found
# a pair of sum k and add it to the output. If not, this element doesn’t belong to a pair yet, and we
# add it to the set of seen elements.
#
# The algorithm is really simple once we figure out using a set. The complexity is O(N) because we do
# a single linear scan of the array, and for each element we just check whether the corresponding number
# to form a pair is in the set or add the current element to the set. Insert and find operations of a set
# are both average O(1), so the algorithm is O(N) in total.

def unique_pairs(arr, k):

    # edge case check
    if len(arr) < 2:
        return

    # Sets for tracking
    seen = set()
    output = set()

    # For every number in array
    for num in arr:

        # Set target difference
        target = k - num

        # Add it to set if target hasn't been seen
        if target not in seen:
            seen.add(num)

        else:
            # Add a tuple with the corresponding pair
            output.add((min(num, target), max(num, target)))

    return '\n'.join(map(str,list(output)))


lst = [1,3,4,6,2,8,10]
k = 5

print(unique_pairs(lst, k))