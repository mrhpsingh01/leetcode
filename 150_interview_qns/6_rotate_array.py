# class Solution:
#     def rotate(self, nums, k: int) -> None:
#         nums = nums[-k:]+nums[:len(nums)-k]
#         return nums
        
list = [-1,-100,3,99]
k = 2
list2 = list[:]

for i in range(len(list)):
    if i < k:
        list[i+k]=list2[i]
        print("if",i,list,list2)
    elif i == k:
        list[0]=list2[]
    else:
        list[i-k-1]=list2[i]
        print("else",i,list)


print(list)