class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        c = 0
    
        while len(prices) > 1:
            p = min(prices)
            k = prices.index(p)
        
            for i in range(k + 1, len(prices)):
                diff = prices[i] - p
                if diff > c:
                    c = diff
                
        # Cut off the checked part so we can check earlier prices next
            prices = prices[:k]
        
        return c

        