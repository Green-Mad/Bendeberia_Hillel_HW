'''You have the file text.txt(attached). Please count how many times each letter appears in this file.'''

file_path = './text.txt'
letter_counts = {}

with open(file_path, 'r') as file:
    text = file.read().lower()

for char in text:
    if char.isalpha():
        letter_counts[char] = letter_counts.get(char, 0) + 1

for letter, count in letter_counts.items():
    print(f"{letter}: {count}")
