def stock_trading(initial_funds, shares_available):
    """
    Simulates a simplified stock trading platform.
    
    :param initial_funds: Initial amount of funds the user has.
    :param shares_available: Dictionary with company names as keys and a tuple of (available shares, price per share) as values.
    :return: A function that processes user transactions.
    """
    user_portfolio = {}
    user_funds = initial_funds

    def process_transaction(transaction_type, company, quantity):
        nonlocal user_funds, shares_available, user_portfolio

        if company not in shares_available:
            return "Company not found."

        available_shares, price_per_share = shares_available[company]

        if transaction_type == "buy":
            total_cost = quantity * price_per_share

            if total_cost > user_funds:
                return "Insufficient funds to buy."

            if quantity > available_shares:
                return "Insufficient shares available to buy."

            # Update funds and shares
            user_funds -= total_cost
            shares_available[company] = (available_shares, price_per_share)

            if company in user_portfolio:
                user_portfolio[company] += quantity
            else:
                user_portfolio[company] = quantity

        elif transaction_type == "sell":
            if company not in user_portfolio or user_portfolio[company] < quantity:
                return "Insufficient shares to sell."

            total_revenue = quantity * price_per_share

            # Update funds and shares
            user_funds += total_revenue
            shares_available[company] = (available_shares + quantity, price_per_share)
            user_portfolio[company] -= quantity

            if user_portfolio[company] == 0:
                del user_portfolio[company]

        else:
            return "Invalid transaction type."

        return {
            "available_shares": shares_available,
            "user_portfolio": user_portfolio.copy(),
            "user_funds": user_funds
        }

    return process_transaction