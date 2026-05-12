class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # time O(n^2)
        # space O(n)
        triplets = set()

        for i in range(len(nums)-1):
            seen = set()
            for j in range(i+1, len(nums)):
                complement = -(nums[i] + nums[j])

                if complement in seen: 
                    answer = tuple(sorted([nums[i],nums[j],complement]))
                    triplets.add(answer)
                seen.add(nums[j])
        
        return list(triplets)



"""
           j 
[-1,0,1,2,-1,-4]
  i 

저장: [0,1,2]
정답: [-1,0,1], [-1,-1,2]

"""