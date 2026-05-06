class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        

        while start <= end: 
            mid = (start + end) // 2
            
            if target == nums[mid]:
                return mid 
            elif target > start: 
                start += 1
            else: 
                end -= 1

        return -1

