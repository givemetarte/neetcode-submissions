class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 아이디어: loop 돌면서 swap하기 
        # 조건1: 양수 범위에 있는 수인가 (배열 벗어나지 않음)
        # 조건2: 제자리에 존재하지 않는가? (존재하면 안 돔)
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]:
                idx = nums[i] - 1
                nums[i], nums[idx] = nums[idx], nums[i]
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1

        return len(nums)+1 

