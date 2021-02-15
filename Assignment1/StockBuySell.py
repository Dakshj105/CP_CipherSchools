def StockBuySell(li):
    profit = 0
    prev = li[0]
    for i in range(1, len(li)):
        if li[i] > prev:
            profit += li[i] - prev
        prev = li[i]
    return profit

li = list(map(int, input().split()))
total_profit = StockBuySell(li)
print(total_profit)