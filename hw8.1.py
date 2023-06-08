#Create a decorator that prints to the console the name of the function that was called. The function should work as
# intended. For example, create a pair of functions for the arithmetic operations of summation and multiplication. When
# calling these functions, the result of the operation must be returned and the name of the function that was called
# must be displayed in the console with the result. Small hint (__name__)
def function_call_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} was called. Result: {result}")
        return result
    return wrapper

@function_call_logger
def add(a, b):
    return a + b

@function_call_logger
def multiply(a, b):
    return a * b

print(add(3, 5))
print(multiply(4, 6))
