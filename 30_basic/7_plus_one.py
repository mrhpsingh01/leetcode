class Solution:
    def plusOne(self, digits):
        if len(digits) == 1 and digits[0] == 9: 
            digits = [1,0] 
            return digits
        if digits[-1] != 9:
            digits[-1] =  digits[-1]+1
        else:
            digits[-1] = 0
            digits[-2] = digits[-2]+1
        return digits



digits = [1,2,9]

x = Solution().plusOne(digits)
print(x)    