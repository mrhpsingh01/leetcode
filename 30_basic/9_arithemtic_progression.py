class Solution:
    def canMakeArithmeticProgression(self, arr) -> bool:
        arr.sort()
        diff = abs(arr[1]-arr[0])
        for i in range(len(arr)-1):
            if abs(arr[i+1]-arr[i]) != diff:
                return False
        return True
        



arr = [-68,-96,-12,-40,16]



x = Solution().canMakeArithmeticProgression(arr)
print(x)    