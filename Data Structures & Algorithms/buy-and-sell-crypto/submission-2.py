class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0 
        buy_pointer, sell_pointer = 0, 1 

        while sell_pointer < len(prices):

            potential_profit =  prices[sell_pointer] - prices[buy_pointer]
            if potential_profit < 0: 
                buy_pointer = sell_pointer
            else: 
                max_profit = max( max_profit, potential_profit)

            sell_pointer +=1

        return max_profit
                

        