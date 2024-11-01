import math


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        num = 0
        if low % 2 == high % 2 == 1:
            num = math.ceil((high - low) / 2) + 1
        else:
            num = math.ceil((high - low) / 2)
        return num


low = 5
high = 10

x = Solution().countOdds(low, high)
print(x)
