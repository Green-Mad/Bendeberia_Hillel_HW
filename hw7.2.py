from typing import Callable, Iterable, List, Any

def my_filter(callback: Callable[[Any], bool], sequence: Iterable) -> List[Any]:
    filtered_elements = []
    for element in sequence:
        if callback(element):
            filtered_elements.append(element)
    return filtered_elements

def is_even(num: int) -> bool:
    return num % 2 == 0

def is_long(word: str) -> bool:
    return len(word) > 5

numbers = [1, 2, 3, 4, 5]
words = ["apple", "banana", "cherry", "orange"]

filtered_numbers = my_filter(is_even, numbers)
print("Filtered even numbers:", filtered_numbers)

filtered_words = my_filter(is_long, words)
print("Filtered long words:", filtered_words)
