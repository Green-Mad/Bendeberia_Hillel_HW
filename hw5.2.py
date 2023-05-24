import pickle

file_path = './test/data/tupelist_data.txt'

with open(file_path, 'rb') as file:
    byte_text = file.read()

result = pickle.loads(byte_text)

for line in result:
    elements = line
    left_operand = int(elements[0])
    right_operand = int(elements[1])
    operation = int(elements[2])

    if operation == 1:
        result = left_operand + right_operand
    elif operation == 2:
        result = left_operand - right_operand
    elif operation == 3:
        result = left_operand * right_operand

    print(result)
