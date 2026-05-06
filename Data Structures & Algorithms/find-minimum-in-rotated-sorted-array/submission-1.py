class Solution:
    def findMin(self, nums: List[int]) -> int:
        # bruce force로 풀기 
        # max = -1 

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        
        return nums[0]
