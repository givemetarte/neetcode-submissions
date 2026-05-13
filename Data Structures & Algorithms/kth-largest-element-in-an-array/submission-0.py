class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_arr = sorted(nums)
        return sorted_arr[len(nums)-k]


"""
[1,2,3,4,5] k=2
> output:4 

# 만약 sorting을 한다면? 
sorted_arr = sorted(nums)  
sorted_arr[len(nums)-k]
len(nums) = 5 
k = 2 
"""