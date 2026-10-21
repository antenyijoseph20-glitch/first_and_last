def receipt_formatter(name, quantity, price):
    quantity = float(quantity)
    price = float(price)

    subtotal = quantity * price
    tax = round(subtotal * 0.075, 2)
    total = round(subtotal + tax, 2)

    return (
        f"Customer: {name}\n"
        f"Subtotal: {float(subtotal)}\n"
        f"Tax: {float(tax)}\n"
        f"Total: {float(total)}"
    )

def solution():
    return receipt_formatter("Joseph", 3, 2000)