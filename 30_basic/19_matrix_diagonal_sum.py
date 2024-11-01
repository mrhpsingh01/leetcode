class Solution:
    def diagonalSum(self, mat: str) -> int:
        sum = 0
        for i, m in enumerate(mat):
            sum = sum + m[i]
            if i != len(m) - i - 1:
                sum = sum + m[len(m) - i - 1]
        return sum


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

x = Solution().diagonalSum(mat)
print(x)
