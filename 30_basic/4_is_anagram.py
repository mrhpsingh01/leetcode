class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        for i in s:                                  ## instead of s put set(s)
            if s.count(i) != t.count(i):
                return False
        return True       

s = "anagram"
t = "nagaram"

x = Solution().isAnagram(s,t)

print(x)