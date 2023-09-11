#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer')\
    .print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
# Test with an empty list
print_reversed_list_integer([])

# Test with a list of one element
print_reversed_list_integer([42])

# Test with a list of negative integers
print_reversed_list_integer([-1, -2, -3, -4, -5])

# Test with a list of mixed positive and negative integers
print_reversed_list_integer([10, -20, 30, -40, 50])

# Test with a list of zeros
print_reversed_list_integer([0, 0, 0, 0, 0])

# Test with a large list
# large_list = list(range(1, 10001))
# print_reversed_list_integer(large_list)
