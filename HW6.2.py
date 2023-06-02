import math
import random
def square(side):
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side
    return perimeter, area, diagonal

if __name__ == "__main__":
    side = random.randint(1, 1000)
    perimeter, area, diagonal = square(side)

print("Perimeter:", perimeter)
print("Area:", area)
print("Diagonal:", diagonal)
