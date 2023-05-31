def display_box(width: int, height: int, character="*"):
    top_bottom_line = character * width
    middle_lines = character + " " * (width - 2) + character
    print(top_bottom_line)
    for _ in range(height - 2):
        print(middle_lines)
    print(top_bottom_line)

display_box(5, 4, 'x')