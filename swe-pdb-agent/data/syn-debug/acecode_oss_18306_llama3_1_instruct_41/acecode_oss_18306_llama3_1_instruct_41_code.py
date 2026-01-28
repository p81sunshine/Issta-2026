# Vending Machine Simulator

def purchase_item(vending_machine, item_name, inserted_money):
    """
    Simulates the behavior of purchasing items from a vending machine.

    Args:
    vending_machine (dict): A dictionary representing the stocked items of the vending machine.
    item_name (str): The name of the item to be purchased.
    inserted_money (float): The amount of money inserted by the user.

    Returns:
    str: A message indicating whether the item was successfully purchased, if it is out of stock, or if the funds are insufficient.
    """

    # Check if the item exists in the vending machine
    if item_name not in vending_machine:
        return 'Item out of stock'

    # Unpack the item's quantity and price from the tuple
    quantity, price = vending_machine[item_name]

    # Check if the item is out of stock
    if quantity <= 0:
        return 'Item out of stock'

    # Check if the inserted money is sufficient
    if inserted_money < price:
        return 'Insufficient funds'

    # Calculate the change to be returned
    change = inserted_money - price

    # Update the item's quantity and calculate the change
    vending_machine[item_name] = (quantity - 1, price)

    # Return the success message with the change
    return f'Dispensing {item_name}. Change: {change:.2f}'

# Test cases
print(purchase_item({'A': (2, 1.5), 'B': (0, 2.0)}, 'A', 2.0))  # Expected output: Dispensing A. Change: 0.50
print(purchase_item({'A': (0, 1.5), 'B': (3, 2.0)}, 'A', 1.5))  # Expected output: Item out of stock