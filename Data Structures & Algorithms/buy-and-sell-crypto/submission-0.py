class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxPro = 0

        while r < len(prices):
            if(prices[l] < prices[r]):
                curPro = prices[r] - prices[l]
                maxPro = max(maxPro, curPro)
            else:
                l = r
            
            r += 1
        
        return maxPro

        