class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0

        #time complexity issue at case number 198
        # for i in range(len(prices)):  
        #     for j in range(len(prices)-i):
        #         if prices[j+i]>prices[i]:
        #             if prices[j+i]-prices[i] > profit:
        #                 profit = prices[j+i]-prices[i]
        #                 print(prices[i],prices[j+i])

        buy = prices[0]
        for p in prices[1:]:
            if buy > p:
                buy = p
            profit = max(profit,p - buy)
        return profit

list = [7,1,5,3,6,4]

x = Solution().maxProfit(list)

print(x)