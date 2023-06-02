def remove_vowels(string):
    vowels = "aeiouyAEIOUY"
    result = ""
    for char in string:
        if char not in vowels:
            result += char
    return result

# Перевірка
# string = "Hello, World!"
# result = remove_vowels(string)
# print(result)
