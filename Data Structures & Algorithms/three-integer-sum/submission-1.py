class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # time O(n^2) | space O(1) (answer 제외하면)
        triplets = set()
        nums.sort()

        for i in range(len(nums)-2): 
            l,h = i+1, len(nums)-1
            
            while l < h: 
                three_sum = nums[i]+nums[l]+nums[h]
                if three_sum > 0: 
                    h -= 1
                elif three_sum < 0: 
                    l += 1
                else: 
                    triplets.add((nums[i],nums[l],nums[h]))
                    l, h = l+1, h-1

        return list(triplets)

"""
아이디어1: 정렬 
아이디어2: 첫번째 두고 두번째 부터 조정 

  i
[-4,-1,-1,0,1,2]
     l        h 

if 세개합 0이면 추가, 0보다 크면 h줄이고, 0보다 작으면 l 줄이기 
세개합 0이면 l과 h 모두 줄이기 
"""