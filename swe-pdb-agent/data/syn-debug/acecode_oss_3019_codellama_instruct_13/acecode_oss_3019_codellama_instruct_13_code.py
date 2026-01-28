import random

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner of a game of rock-paper-scissors.

    Args:
        user_choice (str): The user's choice, either 'rock', 'paper', or 'scissors'.
        computer_choice (str): The computer's choice, randomly generated.

    Returns:
        str: The winner of the game, either 'User wins', 'Computer wins', or 'It's a tie'.
    """
    if user_choice == computer_choice:
        return 'It\'s a tie'
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            return 'Computer wins'
        else:
            return 'User wins'
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            return 'Computer wins'
        else:
            return 'User wins'
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            return 'Computer wins'
        else:
            return 'User wins'
    else:
        raise ValueError('Invalid user choice')

# Tests