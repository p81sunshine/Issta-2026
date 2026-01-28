from typing import List, Tuple

def cell_edit(cells: List[Tuple[str, str]], clicks: List[str]) -> List[str]:
    """
    This function simulates the behavior of a simple spreadsheet cell editor.

    Args:
    cells (List[Tuple[str, str]]): A list of tuples, where each tuple represents a cell in the format (tag, content).
    clicks (List[str]): A list of tags representing the order in which the cells are clicked.

    Returns:
    List[str]: A list of strings representing the status updates for each cell click in the order they were clicked.
    """
    # Create a dictionary to store the state of each cell
    cell_state = {cell[0]: cell for cell in cells}

    # Initialize an empty list to store the status updates
    status_updates = []

    # Iterate over the clicks
    for click in clicks:
        # Check if the clicked cell exists
        if click in cell_state:
            # Get the tag and content of the clicked cell
            tag, content = cell_state[click]

            # Update the status of the clicked cell to 'being edited'
            cell_state[click] = (tag, content, 'being edited')

            # Append the status update to the list
            status_updates.append(f'clicked on cell tag {tag}, content {content}')
        else:
            # If the clicked cell does not exist, append a message to the list
            status_updates.append(f'clicked on non-existent cell tag {click}')

    return status_updates

# Test the function
print(cell_edit([('A1', 'Hello'), ('A2', 'World')], ['A1', 'A2']))
# Output: ['clicked on cell tag A1, content Hello', 'clicked on cell tag A2, content World']

print(cell_edit([('B1', 'Data'), ('B2', 'Science')], ['B2']))
# Output: ['clicked on cell tag B2, content Science']