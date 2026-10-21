
def exact_calculator(left, operator, right):
    try:
        left = float(left)
        right = float(right)
    except (ValueError, TypeError):
        return "Invalid number"

    if operator not in ["+", "-", "*", "/", "%", "**"]:
        return "Invalid operator"

    if operator in ["/", "%"] and right == 0:
        return "Cannot divide by zero"

    if operator == "+":
        result = left + right
    elif operator == "-":
        result = left - right
    elif operator == "*":
        result = left * right
    elif operator == "/":
        result = left / right
    elif operator == "%":
        result = left % right
    else:
        result = left ** right

    return round(result, 2)
