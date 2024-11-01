class Solution:
    def arraySign(self, nums) -> int:
        if nums.count(0) > 0: return 0
        count = 0
        nums.sort()
        for i in nums:
            if i < 0:
                count+=1
            
        if count%2==0:
            return 1
        else:
            return -1



nums = [-5]

x = Solution().arraySign(nums)
print(x)    