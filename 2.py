
""""
2)Best Time to Buy and Sell Stock (121)

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
 
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
"""


#easy begginer level program
prices = [7,1,6,3,5,9]

max_profit = 0

for i in range(len(prices)):
    for j in range(i+1, len(prices)):

        profit = prices[j] - prices[i]

        if profit > max_profit:
            max_profit = profit

print(max_profit)



#interview level or coding level program

prices_1 = [7,1,6,3,4,9]

min_price = prices_1[0]
max_profit_1 = 0

for price in prices_1:

    if price < min_price:
        min_price = price

    profit_1 = price - min_price

    if profit_1 > max_profit_1:
        max_profit_1 = profit_1

print(max_profit_1)


