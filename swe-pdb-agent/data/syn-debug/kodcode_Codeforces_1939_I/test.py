from solution import *

import math

from solution import *

import math

from solution import *

import math

import pytest
from solution import process_commands

def test_add_and_display():
    commands = [
        "ADD BOOK The_Great_Gatsby F_Scott_Fitzgerald 9780743273565 5",
        "ADD MAGAZINE Time 202307 10",
        "ADD BOOK War_and_Peace Leo_Tolstoy 9780198800545 3",
        "DISPLAY"
    ]
    output = process_commands(4, commands)
    expected_output = (
        "Books:\n"
        "Title: The_Great_Gatsby, Author: F_Scott_Fitzgerald, ISBN: 9780743273565, Quantity: 5\n"
        "Title: War_and_Peace, Author: Leo_Tolstoy, ISBN: 9780198800545, Quantity: 3\n\n"
        "Magazines:\n"
        "Title: Time, Issue: 202307, Quantity: 10"
    )
    assert output == expected_output

def test_update_and_display():
    commands = [
        "ADD BOOK The_Great_Gatsby F_Scott_Fitzgerald 9780743273565 5",
        "ADD MAGAZINE Time 202307 10",
        "ADD BOOK War_and_Peace Leo_Tolstoy 9780198800545 3",
        "UPDATE BOOK 9780743273565 7",
        "UPDATE MAGAZINE 202307 5",
        "DISPLAY"
    ]
    output = process_commands(6, commands)
    expected_output = (
        "Books:\n"
        "Title: The_Great_Gatsby, Author: F_Scott_Fitzgerald, ISBN: 9780743273565, Quantity: 7\n"
        "Title: War_and_Peace, Author: Leo_Tolstoy, ISBN: 9780198800545, Quantity: 3\n\n"
        "Magazines:\n"
        "Title: Time, Issue: 202307, Quantity: 5"
    )
    assert output == expected_output

def test_invalid_commands():
    commands = [
        "INVALID 001",
        "ADD BOOK Valid_Book Author 12345 10",
        "UPDATE BOOK 12345 15",
        "UPDATE MAGAZINE 67890 5",
        "DISPLAY"
    ]
    output = process_commands(5, commands)
    expected_output = (
        "Books:\n"
        "Title: Valid_Book, Author: Author, ISBN: 12345, Quantity: 15\n\n"
        "Magazines:"
    )
    assert output == expected_output

def test_empty_inventory():
    commands = [
        "DISPLAY"
    ]
    output = process_commands(1, commands)
    expected_output = (
        "Books:\n\n"
        "Magazines:"
    )
    assert output == expected_output