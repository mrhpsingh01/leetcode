class Solution:
    def moveZeroes(self, nums) -> None:
        loop = True
        i=0
        n = len(nums)-1
        if nums.count(0) == 0: return nums
        while n != 0:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                n=n-1
            else:
                i=i+1
        return nums



nums = [2,1]

x = Solution().moveZeroes(nums)

print(x)