class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])


s = "   fly me   to   the moon  "


x = Solution().lengthOfLastWord(s)
print(x)
