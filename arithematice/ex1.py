
def safe_calculator(a, operator, b):
    if operator not in ["+", "-", "*", "/", "%", "**"]:
        return "Invalid operator"

    if operator in ["/", "%"] and b == 0:
        return "Cannot divide by zero"

    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return round(a / b, 2)
    elif operator == "%":
        return a % b
    elif operator == "**":
        return a ** b
