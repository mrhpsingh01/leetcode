class Solution:
    def maximumWealth(self, accounts: str) -> bool:
        maximum = 0
        for wealth in accounts:
            maximum = max(maximum, sum(wealth))
        return maximum


accounts = [[1, 2, 3], [3, 2, 1]]

x = Solution().maximumWealth(accounts)
print(x)
