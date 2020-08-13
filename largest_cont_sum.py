# Given an array of integers (positive and negative) find the largest continuous sum.

def l_sum(ar):

    # Check to see if array is length 0
    if len(ar) == 0:
        return None

    # Start the max and current sum at the first element
    sum_current = sum_max = ar[0]

    # For every element in array
    for num in ar[1:]:
        # Set current sum as the higher of the two
        sum_current = max(sum_current + num, num)

        # Set max as the higher between the currentSum and the current max
        sum_max = max(sum_current, sum_max)

    return sum_max

ar = [1,2,-1,3,4,10,10,-10,-1]

print(l_sum(ar))

