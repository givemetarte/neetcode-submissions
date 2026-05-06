class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)

        before = 1
        for i in range(len(nums)-1):
            before *= nums[i]
            products[i+1] *= before

        after = 1
        for j in range(len(nums)-1,0,-1):
            after *= nums[j]
            products[j-1] *= after

        return products