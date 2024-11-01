class Solution:
    def largestPerimeter(self, nums) -> int:
        # perimeter = 0
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         for k in range(len(nums)):
        #             if i != j and j != k and i != k:
        #                 if (
        #                     nums[i] + nums[j] > nums[k]
        #                     and nums[j] + nums[k] > nums[i]
        #                     and nums[i] + nums[k] > nums[j]
        #                     and nums[i] + nums[j] + nums[k] > perimeter
        #                 ):
        #                     perimeter = nums[i] + nums[j] + nums[k]
        # return perimeter
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0


nums = [1, 2, 1, 10]


x = Solution().largestPerimeter(nums)
print(x)
