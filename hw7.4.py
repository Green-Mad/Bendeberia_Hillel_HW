def my_max(iterable, amount=1):
    if amount == 1:
        max_value = iterable[0]
        for item in iterable:
            if item > max_value:
                max_value = item
        return max_value
    else:
        sorted_values = sorted(iterable, reverse=True)
        return sorted_values[:amount]

def my_min(iterable, amount=1):
    if amount == 1:
        min_value = iterable[0]
        for item in iterable:
            if item < min_value:
                min_value = item
        return min_value
    else:
        sorted_values = sorted(iterable)
        return sorted_values[:amount]

numbers = [6, 4, 3, 7, 2, 8, 1, 0, 6, 42, 3, 1]

max_value = my_max(numbers)
print("Max value:", max_value)

min_value = my_min(numbers)
print("Min value:", min_value)

max_values = my_max(numbers, amount=2)
print("Two max values:", max_values)

min_values = my_min(numbers, amount=3)
print("Thre min values:", min_values)
