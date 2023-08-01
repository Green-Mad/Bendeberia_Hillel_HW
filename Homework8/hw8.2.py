# Create a function that can return the squares of even elements for the range 0 to 1000000000 inclusive. The solution
# should work and not freeze your computer.

def even_squares_generator():
    for number in range(1000000001):
        if number % 2 == 0:
            yield number ** 2

squares = even_squares_generator()

for _ in range(10):
    print(next(squares))
