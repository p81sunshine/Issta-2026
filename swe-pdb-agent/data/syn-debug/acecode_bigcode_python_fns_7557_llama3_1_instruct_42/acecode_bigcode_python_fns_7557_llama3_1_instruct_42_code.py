# asset_dividend_record.py

def asset_dividend_record(asset: str, start_time: int, end_time: int, limit: int, recv_window: int = None) -> list:
    """
    Simulates querying an asset dividend record for a user.

    Args:
        asset (str): Asset string.
        start_time (int): Start time integer.
        end_time (int): End time integer.
        limit (int): Limit integer.
        recv_window (int, optional): Receive window integer. Defaults to None.

    Returns:
        list: A list of strings formatted as 'Asset: {asset}, Start Time: {start_time}, End Time: {end_time}, Limit: {limit}'.
    """

    # Check if start time is greater than end time
    if start_time > end_time:
        return ['Start time must be less than end time']

    # Check if limit exceeds maximum allowed (500)
    if limit > 500:
        return ['Limit exceeds maximum allowed']

    # Check if receive window exceeds maximum allowed (60000)
    if recv_window is not None and recv_window > 60000:
        return ['Receive window exceeds maximum allowed']

    # Return the formatted string
    return [f'Asset: {asset}, Start Time: {start_time}, End Time: {end_time}, Limit: {limit}']

# Test cases
print(asset_dividend_record('BTC', 1610000000, 1620000000, 20))
print(asset_dividend_record('ETH', 1600000000, 1610000000, 500))
print(asset_dividend_record('Asset', 1610000000, 1600000000, 20))  # Test start_time > end_time
print(asset_dividend_record('Asset', 1610000000, 1620000000, 600))  # Test limit > 500
print(asset_dividend_record('Asset', 1610000000, 1620000000, 20, 70000))  # Test recv_window > 60000