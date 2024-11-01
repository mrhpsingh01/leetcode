class Solution:
    def canJump(self, nums) -> bool:
        jump = True
        i=0
        while jump:
            if i == len(nums)-1:
                break
            if i > len(nums)-1:
                jump = False
            if i < len(nums):
                if nums[i] == 0:
                    jump = False
            i = i + nums[i]
            
        return jump




list = [2,0]

x = Solution().canJump(list)

print(x)