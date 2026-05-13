class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # time O(logn): 이중 탐색 
        # space O(1)
        l, h = 0, len(nums)-1 

        while l <= h: 
            m = (l + h) // 2 

            if nums[m] == target: 
                return m 
            
            if nums[l] <= nums[m]: # 왼쪽 확실히 정렬 
                if nums[l] <= target < nums[m]:
                    h = m -1
                else: 
                    l = m + 1
            else: 
                if nums[m] < target <= nums[h]:
                    l = m -1
                else: 
                    h = m + 1
        return -1 



"""
 l   m     r
[3,4,5,6,1,2]

 l   m     r
[3,5,6,0,1,2] 4

"""