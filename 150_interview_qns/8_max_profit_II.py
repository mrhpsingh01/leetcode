class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        buy = prices[0]
        total = 0
        for p in prices[1:]:
            if buy > p:
                buy = p
            profit = max(profit,p - buy)
        return profit

list = [7,1,5,3,6,4]

x = Solution().maxProfit(list)

print(x)