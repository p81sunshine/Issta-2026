def send_message(recipient: str, message_type: str, content: str) -> str:
    """
    Sends a message to the specified recipient based on the message type.

    Args:
    - recipient (str): The recipient's email address, phone number, or user ID.
    - message_type (str): The type of message to be sent ('email', 'sms', 'mms', or 'notification').
    - content (str): The content of the message.

    Returns:
    - str: A string indicating the success of the message sent. If the message type is invalid, it returns 'Invalid message type'.
    """
    # Define a dictionary to map message types to their corresponding sending functions
    sending_functions = {
        'email': send_email,
        'sms': send_sms,
        'mms': send_mms,
        'notification': send_notification
    }

    # Check if the message type is valid
    if message_type in sending_functions:
        # Call the corresponding sending function and return its result
        return sending_functions[message_type](recipient, content)
    else:
        # Return 'Invalid message type' if the message type is invalid
        return 'Invalid message type'


# Define the sending functions for each message type
def send_email(recipient: str, content: str) -> str:
    """
    Sends an email to the specified recipient.

    Args:
    - recipient (str): The recipient's email address.
    - content (str): The content of the email.

    Returns:
    - str: A string indicating the success of the email sent.
    """
    return f'Email sent successfully to {recipient}'


def send_sms(recipient: str, content: str) -> str:
    """
    Sends an SMS to the specified recipient.

    Args:
    - recipient (str): The recipient's phone number.
    - content (str): The content of the SMS.

    Returns:
    - str: A string indicating the success of the SMS sent.
    """
    return f'SMS sent successfully to {recipient}'


def send_mms(recipient: str, content: str) -> str:
    """
    Sends an MMS to the specified recipient.

    Args:
    - recipient (str): The recipient's phone number.
    - content (str): The content of the MMS.

    Returns:
    - str: A string indicating the success of the MMS sent.
    """
    return f'MMS sent successfully to {recipient}'


def send_notification(recipient: str, content: str) -> str:
    """
    Sends a notification to the specified recipient.

    Args:
    - recipient (str): The recipient's user ID.
    - content (str): The content of the notification.

    Returns:
    - str: A string indicating the success of the notification sent.
    """
    return f'Notification sent successfully to {recipient}'

# Test the function