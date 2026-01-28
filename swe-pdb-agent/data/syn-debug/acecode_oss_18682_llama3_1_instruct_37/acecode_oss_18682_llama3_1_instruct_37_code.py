def inventory_management(operations):
    """
    Simulates a simple inventory management system for a small retail store.

    Args:
    operations (list): A list of operations on the inventory, where each operation is represented as a tuple.

    Returns:
    dict: The current inventory status as a dictionary after performing all operations.

    """
    # Initialize an empty dictionary to represent the inventory
    inventory = {}

    # Iterate over each operation in the list of operations
    for op in operations:
        # Extract the operation type and other parameters from the tuple
        op_type, *params = op

        # Handle the 'add_product' operation
        if op_type == 'add':
            # Extract the product name and quantity from the parameters
            product_name, quantity = params
            # Add the product to the inventory or update the quantity if it already exists
            inventory[product_name] = inventory.get(product_name, 0) + quantity

        # Handle the 'remove_product' operation
        elif op_type == 'remove':
            # Extract the product name from the parameters
            product_name = params[0]
            # Remove the product from the inventory if it exists
            if product_name in inventory:
                del inventory[product_name]

        # Handle the 'update_quantity' operation
        elif op_type == 'update':
            # Extract the product name and new quantity from the parameters
            product_name, new_quantity = params
            # Update the quantity of the product in the inventory
            inventory[product_name] = new_quantity

    # Return the current inventory status as a dictionary
    return inventory

# Test the function