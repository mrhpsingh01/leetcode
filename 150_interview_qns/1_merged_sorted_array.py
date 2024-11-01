class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        for i in range(n):
            nums1[m+i] = list2[i]
        Solution.quickSort(nums1,0,m+n)
        
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                Solution.swap(arr, i, j)
        Solution.swap(arr, i + 1, high)
        return i + 1

    def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def quickSort(arr, low, high):
        if low < high:
            pi = Solution.partition(arr, low, high)            
            Solution.quickSort(arr, low, pi - 1)
            Solution.quickSort(arr, pi + 1, high)


list = [4,5,6,0,0,0]
m = 3
list2 = [1,2,3]
n = 3
             
                        
Solution().merge(list,m,list2,n)