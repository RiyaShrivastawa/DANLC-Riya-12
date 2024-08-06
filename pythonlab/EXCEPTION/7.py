class OutOfStockError(Exception):
    pass
class InvalidOrderError(Exception):
    pass
def process_order(order, stock):
    for item, quantity in order.items():
        if quantity <= 0:
            raise InvalidOrderError(
                f"Invalid quantity for item '{item}': {quantity}. Quantity must be greater than zero.")
        if item not in stock:
            raise OutOfStockError(f"Item '{item}' is not available in stock.")
        if stock[item] < quantity:
            raise OutOfStockError(
                f"Insufficient stock for item '{item}': requested {quantity}, available {stock[item]}.")

        print(f"Processing {quantity} of '{item}'")

    print("Order processed successfully.")

stock = {
    "apple": 10,
    "banana": 5,
    "orange": 0
}

orders = [
    {"apple": 3, "banana": 2},
    {"apple": 11},
    {"orange": 1},
    {"banana": -1},
    {"apple": 5, "pear": 2}
]

for order in orders:
    try:
        process_order(order, stock)
    except (OutOfStockError, InvalidOrderError) as e:
        print(f"Order processing failed: {e}")