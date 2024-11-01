class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for l in t:
            if s.count(l) != t.count(l):
                return l
            
        

s = "a"
t = "aa"

x = Solution().findTheDifference(s,t)

print(x)