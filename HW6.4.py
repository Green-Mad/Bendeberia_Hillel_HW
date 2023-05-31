import re

file_path =
def remove_numbers_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        updated_line = re.sub(r'\d+', '', line)  # Remove all numbers from the line
        updated_lines.append(updated_line)

    with open(file_path, 'w') as file:
        file.writelines(updated_lines)
