"""
time: n + n/2 + n/4 + n/8 + ... = 2n = O(n)
space: O(log(n))
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def find_at(low, high, idx):
            pivot = partition(low, high)
            if idx < pivot: 
                return find_at(low, pivot-1, idx)
            if idx > pivot: 
                return find_at(pivot+1, high, idx)
            return nums[idx]
        
        def partition(low, high): 
            p = low 
            for i in range(low, high):
                if nums[i] < nums[high]:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[high], nums[p] = nums[p], nums[high]
            return p
        
        return find_at(0, len(nums)-1, len(nums)-k)

"""
                l k
nums = [3,2,1,4,5,6], k = 2 
                p
"""