# Implement your own all function
def my_all(iterable):
    for element in iterable:
        if not element:
            return False
    return True

numbers = [2, 4, 6, -15, 4.3]
res = my_all(number > 0 for number in numbers)
print('Numbers are float:', res)