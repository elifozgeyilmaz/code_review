# Write your corrected implementation for Task 1 here.
# Do not modify `task1.py`.
"""
def calculate_average_order_value(orders):
    total = 0
    count = len(orders)

    for order in orders:
        if order["status"] != "cancelled":
            total += order["amount"]

    return total / count


"""


def calculate_average_order_value(orders):
    total = 0.0
    valid_count = 0

    for order in orders:
        try:
            if order.get("status") == "cancelled":
                continue

            amount = order.get("amount")
            if amount is None:
                continue

            value = float(amount)
            if value <= 0:
                continue

            total += value
            valid_count += 1
        except (TypeError, ValueError):
            continue
    # if there are no orders, we need to check otherwise division by 0 error will occur
    if(valid_count>0):
        return total / valid_count
    else:
        return 0
