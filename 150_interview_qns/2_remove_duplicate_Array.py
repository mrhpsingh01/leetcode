class Solution:
    def removeElement(self, nums, val: int) -> int:
        while nums.count(val):
            nums.pop(nums.index(val))
        return len(nums)
    

list = [0,1,2,2,3,0,4,2]
m = 2

Solution().removeElement(list,m)