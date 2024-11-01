class Solution:
    def majorityElement(self, nums) -> int:
        max = 0
        maxNum = 0
        nums.sort()
        for i in range(len(nums)):
            if i >0:
                if nums[i] == nums[i-1]:
                    pass
                else:
                    if nums.count(nums[i])>max:
                        max = nums.count(nums[i])
                        maxNum = nums[i]
            else:
                max = nums.count(nums[i])
                maxNum = nums[i]
                
        return maxNum

list = [6,5,5]

x = Solution().majorityElement(list)

print(x)