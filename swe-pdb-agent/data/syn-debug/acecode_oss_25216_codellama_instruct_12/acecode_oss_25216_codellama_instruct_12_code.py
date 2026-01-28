def manage_connection(commands):
    """
    Simulates a simple database connection manager.

    Parameters
    ----------
    commands : list of strings
        A list of strings representing commands to either open or close a
        connection, or to check if the connection is currently open.

    Returns
    -------
    list of booleans
        A list of boolean values indicating the result of each command.

    Raises
    ------
    ConnectionError
        If the connection is already open when an 'open' command is issued,
        or if no connection is open when a 'close' command is issued.
    """
    connection_status = False  # initial state of the connection is closed
    result = []
    for command in commands:
        if command == 'open':
            if connection_status:
                raise ConnectionError('Connection already open')
            connection_status = True
            result.append(True)
        elif command == 'close':
            if not connection_status:
                raise ConnectionError('No connection to close')
            connection_status = False
            result.append(True)
        elif command == 'status':
            result.append(connection_status)
        else:
            raise ValueError(f'Invalid command: {command}')
    return result


# Tests

# Command: 'open'