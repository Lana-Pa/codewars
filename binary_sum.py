# Implement a function that adds two numbers together and returns their sum in binary.
# The conversion can be done before, or after the addition.
#
# The binary number returned should be a string.

# using built-in function
def add_binary(a,b):
    return bin(a+b)[2:]

# format option
def add_binary(a,b):
    return '{0:b}'.format(a + b)

# using recursion
def convert_dec_bin(num):
    if num >= 1:
        convert_dec_bin(num//2)
        print(num % 2, end='')

def add_binary(a,b):
    sum = a+b
    convert_dec_bin(sum)


add_binary(51,12)