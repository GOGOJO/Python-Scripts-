def max_profit_days(stock_prices):
    # Write your code here:
    profit = 0
    indexs = []
    for i in range(len(stock_prices)):
        for j in range(i + 1, len(stock_prices)):
            current_profit = 0
            if stock_prices[j] > stock_prices[i]:
                current_profit = stock_prices[j] - stock_prices[i]
            if max(profit, current_profit) == current_profit:
                profit = current_profit
                indexs.clear()
                indexs.append(i)
                indexs.append(j)

    return (indexs[0], indexs[1])


print(max_profit_days([4, 20, 10]))
