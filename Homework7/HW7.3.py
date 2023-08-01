# Implement your own implementation of the function map

from typing import Callable, Iterable, List, Any

def my_map(callback: Callable[[Any], Any], sequence: Iterable) -> List[Any]:
    mapped_elements = []
    for element in sequence:
        mapped_elements.append(callback(element))
    return mapped_elements
def square_number(num: int) -> int:
    return num ** 2

def capitalize_word(word: str) -> str:
    return word.capitalize()

numbers = [1, 2, 3, 4, 5]
words = ["apple", "banana", "cherry", "orange"]

mapped_numbers = my_map(square_number, numbers)
print("Mapped numbers:", mapped_numbers)

mapped_words = my_map(capitalize_word, words)
print("Mapped words:", mapped_words)
