def arithmetic(left_operand, right_operand, operation):
    """Perform arithmetic operation on two numbers.
    Args:
        left_operand (int or float): The left operand.
        right_operand (int or float): The right operand.
        operation (str): The operation to be performed ('+', '-', '*', or '/').
    Returns:
        int or float or str: The result of the arithmetic operation, or a string indicating an unknown operation."""
    if operation == '+':
        return left_operand + right_operand
    elif operation == '-':
        return left_operand - right_operand
    elif operation == '*':
        return left_operand * right_operand
    elif operation == '/':
        return left_operand / right_operand
    else:
        return f"Not known operation: {operation}"


if __name__ == "__main__":
    assert arithmetic(3, 4, operation="*") == 12
    assert arithmetic(3, 4, operation="+") == 7
    assert arithmetic(25, 5, operation="/") == 5
    assert type(arithmetic(25, 5, operation="/")) == float
    assert arithmetic(5, 5, operation="//") == "Not known operation: //"
    assert arithmetic.__doc__ == """Perform arithmetic operation on two numbers.
    Args:
        left_operand (int or float): The left operand.
        right_operand (int or float): The right operand.
        operation (str): The operation to be performed ('+', '-', '*', or '/').
    Returns:
        int or float or str: The result of the arithmetic operation, or a string indicating an unknown operation."""
    assert arithmetic.__code__.co_name == "arithmetic"
    assert arithmetic.__code__.co_varnames == ("left_operand", "right_operand", "operation")
    try:
        arithmetic(1, 2, 3)
    except TypeError as e:
        assert e.__class__ is TypeError
    try:
        arithmetic(left_operand=1, right_operand=2, operation="+")
    except TypeError as e:
        assert e.__class__ is TypeError

    try:
        arithmetic(1, right_operand=2, operation="+")
    except TypeError as e:
        assert e.__class__ is TypeError

print("All checks passed successfully.")
