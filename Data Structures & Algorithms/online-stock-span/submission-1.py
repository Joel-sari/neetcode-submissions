"""

Span of Stock = max number of consecutive days ( from that day and backward) for which the stock has been doing great (increasing or stuck = prices before are less than or equal to) 



"""

class StockSpanner:

    def __init__(self):

        self.stocks_every_day = []

        

    def next(self, price: int) -> int:
        # add the price to the array of stocks
        self.stocks_every_day.append(price)

        current_stock =  self.stocks_every_day[-1]

        index = len(self.stocks_every_day) - 1 

        # current span or days in which we have been up, includes your price/day
        span = 1 

        while (index - 1) > -1 and index > -1 and self.stocks_every_day[index - 1] <= current_stock: 
            span += 1 
            index -= 1
        
        
        return span
    
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)