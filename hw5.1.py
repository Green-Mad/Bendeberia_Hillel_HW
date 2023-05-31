'''Create a list of tuples with a length of 100 elements where each tuple consists of 3 elements:
a. element is an integer that will be the left operand of the expression
b. element is an integer that will be the right operand of the expression
c. element is an integer from 1 to 3 where:

- identifies the addition operation
- identifies the subtraction operation
- identifies the multiplication operation

d. You can put data into a text file with the text form or use the pickle module in binary form. If placed as text then
each line should contain only elements of one tuple separated by spaces (eg "100 2 3"). The file must be created by a
script in a pre-created \test\data directory tree. The directory tree must be created by the script. Push only the code
to the repository (not directories or file).'''

import random
import os


os.makedirs('test/data', exist_ok=True)


operations = [1, 2, 3]
tupelist = []

for _ in range(100):
    left_operand = random.randint(1, 100)
    right_operand = random.randint(1, 100)
    operation = random.choice(operations)
    tupelist.append((left_operand, right_operand, operation))


file_path = './test/data/tupelist_data.txt'
with open(file_path, 'w') as file:
    for tpl in tupelist:
        file.write(f"{tpl[0]} {tpl[1]} {tpl[2]}\n")

print("Data added successfully", file_path)


import pickle
with open (file_path, 'w+b') as file:
    data_to_write = pickle.dumps(tupelist)
    file.write(data_to_write)
