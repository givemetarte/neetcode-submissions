class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # 일단 최댓값을 추출한 후 그 최댓값에 대해 루프를 돌면서 nums에 있는지 판단 
        max_num = max(nums)

        # 0보다 작거나 같다면 1추출 
        if max_num <= 0: 
            return 1 

        # max_num만큼 리스트 채우기 
        # 루프 돌면서 max num 있는지 없는지 판단 
        # cols = [0,0,0,0,0,0,0]
        cols = [0] * (max_num+1)

        # cols = [0,1,1,1,1,1,1]
        for num in nums: 
            cols[num] = 1
        
        # i=1 > cols[1] = 1 > pass
        # i=2 > cols[2] = 1 > pass 
        # 아 이경우는 다 돌았음 

        i = 1 
        while i < len(cols):
            if cols[i] == 0:
                return i
            i += 1 
        
        return len(cols)







            