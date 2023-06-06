# Find all of the numbers from 1-1000 that are divisible by 7

divisible_by_7 = []

for number in range(1, 1001):
    if number % 7 == 0:
        divisible_by_7.append(number)

print(divisible_by_7)
