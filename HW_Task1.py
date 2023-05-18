elements = [1, 2, 3, 4, 5, 6, 7, 8]
odd_elements = []
even_elements = []

for index, value in enumerate(elements):
    if index % 2 == 0:
        odd_elements.append((index, value))
    else:
        even_elements.append((index, value))

print('Odd elements:', odd_elements)
print('Even elements:', even_elements)
