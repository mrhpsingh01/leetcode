class Solution:
    def isMonotonic(self, nums) -> bool:
        if len(nums) == 1:
            return True
        if nums[1] - nums[0] > 0:
            for i in range(len(nums) - 1):
                if nums[i + 1] - nums[i] < 0:
                    return False
        elif nums[1] - nums[0] == 0:
            if (len(nums)) == 2:
                return True
            if nums[2] - nums[1] > 0:
                for i in range(len(nums) - 1):
                    if nums[i + 1] - nums[i] < 0:
                        return False
            else:
                for i in range(len(nums) - 1):
                    if nums[i + 1] - nums[i] > 0:
                        return False
        else:
            for i in range(len(nums) - 1):
                if nums[i + 1] - nums[i] > 0:
                    return False
        return True


nums = [-5, -5, -5, -5, -2, -2, -2, -1, -1, -1, 0]


x = Solution().isMonotonic(nums)
print("asd", x)
