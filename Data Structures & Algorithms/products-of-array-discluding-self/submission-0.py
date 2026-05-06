import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answers = []

        for i in range(len(nums)):
            others = nums[:i] + nums[i+1:]
            answers.append(math.prod(others))
        return answers

