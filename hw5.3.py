'''You have the file text.txt(attached). Please count how many times each letter appears in this file.'''

file_path = './text.txt'
letter_counts = {}

with open(file_path, 'r') as file:
    for line in file:
        for char in line:
            if char.isalpha():
                char = char.lower()
                if char in letter_counts:
                    letter_counts[char] += 1
                else:
                    letter_counts[char] = 1

for letter, count in letter_counts.items():
    print(f"{letter}: {count}")
