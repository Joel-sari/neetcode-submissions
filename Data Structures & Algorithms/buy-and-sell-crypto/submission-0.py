class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # create two pointers next to eachother 
        r = 1  #right will represent a high selling point
        l = 0  #left will represent a low buying point
        max_price = 0 
        while r < len(prices): 
            


            # if day n price is lower then day n + 1 (GOOD THING), left pointer remains, else we also move left pointer 
            if prices[l]< prices[r]:
                profit = prices[r]-prices[l]
                if max_price < profit:
                    max_price = max(max_price, profit)
            else:
                l = r
            r += 1
        return max_price


                



        