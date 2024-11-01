class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int(a), int(b)
        n = len(a) if len(a) > len(b) else len(b)
        sum = ""
        
        for i in range(n):
            if a[-i] == "1" and b[-i] == "1":
                sum
                print(a[-i])
        return True


a = "1010"
b = "1011"

x = Solution().addBinary(a, b)
print(x)
