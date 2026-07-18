class Solution:

    #We can perform any number of transactions!
    #This may mean we can sell multiple times, meaning anytime their is even a little bit of profit 
    # We then just update our pointer accordingly

    """
    Think about this in way of stocks, we gain much more of profit making many transactions 
    that involve multiple big profit sales rather than one big one.\

    so we need to keep checking in the future! ensuring that we are at the local maximum 
    
    """ 
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i -1]:
                profit += prices[i] - prices[i-1]
        return profit

        



        

             
        



        