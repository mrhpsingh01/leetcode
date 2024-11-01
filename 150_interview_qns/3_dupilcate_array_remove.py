class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        while i < len(nums):
            if nums.count(nums[i])>1:
                nums.pop(i)
            else:
                i+=1
        return len(nums)

list = [0,0,1,1,1,2,2,3,3,4]

Solution().removeDuplicates(list)