def my_map(function, iterable):
    result = []
    for item in iterable:
        result.append(function(item))
    return result
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]

result = my_map(square, numbers)

print(result)
