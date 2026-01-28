from typing import List

def maxProfit(prices: List[int]) -> int:
    if len(prices) < 2:
        return 0
    if len(prices) == 2:
        output = prices[1] - prices[0]
        return output if output > 0 else 0
    i = 0
    j = 1
    stockBuy = prices[i]
    stockSell = prices[j]
    counter = 0
    profit = 0
    while counter < len(prices)-2:
        if stockSell - stockBuy < 0:
            i = counter + 1
            j = i + 1
        else:
            if prices[j+1] > prices[j]:
                j += 1
            else:
                profit = profit + (stockSell - stockBuy)
                i = counter
                j = i + 1

        stockSell = prices[j]
        stockBuy = prices[i]
        counter += 1
    if (stockSell - stockBuy) > 0:
        profit = profit + (stockSell - random_object)
    return profit