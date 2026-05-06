class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_nums = len(set(nums))

        if new_nums < len(nums):
            return True
        else: 
            return False