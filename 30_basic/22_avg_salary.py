class Solution:
    def average(self, salary) -> int:
        salary.sort()
        salary.pop()
        salary.pop(0)
        return sum(salary) / len(salary)


salary = [4000, 3000, 1000, 2000]

x = Solution().average(salary)
print(x)
