import random
def is_prime(number):
    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True

number = random.randint(2, 1000)
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
