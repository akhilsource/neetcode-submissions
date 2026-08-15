class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min1=float('inf')
        maxp=0
        for i in range(len(prices)):
            min1=min(min1,prices[i])
            profit=prices[i]-min1
            maxp=max(maxp,profit)
        return maxp