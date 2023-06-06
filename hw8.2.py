# Create a function that can return the squares of even elements for the range 0 to 1000000000 inclusive. The solution
# should work and not freeze your computer.

def even_squares():
    num = 0
    while num <= 1000000000:
        yield num**2
        num += 2

even_squares_generator = even_squares()

for square in even_squares_generator:
    print(square)
