def my_filter(function, iterable):
    filtered_list = [item for item in iterable if function(item)]
    return filtered_list

# для прикладу

# def is_even(num):
#     return num % 2 == 0
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filtered_numbers = my_filter(is_even, numbers)
# print(filtered_numbers)

print(my_filter)
