from typing import List
from collections import defaultdict

def invalidTransactions(transactions: List[str]) -> List[str]:
    invalid = []
    txn = defaultdict(list)
    
    for trn in transactions:
        name, time, amount, city = trn.split(",")
        txn[name].append([time, amount, city])
    
    for trans in range(len(transactions)):
        name, time, amount, city = transactions[trans].split(",")
        if int(amount) > 10000:
            invalid.append(transactions[trans])
        else:
            for trn in txn[name]:
                time_i, _, city_i = trn
                if city != city_i and abs(int(time) - int(time_i)) <= 60:
                    invalid.append(transactions[trans])
                    break

    return invalid