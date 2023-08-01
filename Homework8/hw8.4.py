# Find all of the numbers from 1-1000 that have a 3 in them

numbers_with_3 = (number for number in range(1, 1001) if '3' in str(number))
print(list(numbers_with_3))
