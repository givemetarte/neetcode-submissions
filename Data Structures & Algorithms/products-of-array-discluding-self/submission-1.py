class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 누적합 아이디어 떠올리기 
        # before 왼쪽에서 곱셈, right 오른쪽에서 곱셈 
        before = [1] * len(nums)
        for i in range(len(nums)-1):
            before[i+1] = before[i]*nums[i]

        after = [1] * len(nums)
        for j in range(len(nums)-1,0,-1):
            after[j-1] = after[j]*nums[j]

        products = []
        for a,b in zip(before, after):
            products.append(a*b)
        
        return products