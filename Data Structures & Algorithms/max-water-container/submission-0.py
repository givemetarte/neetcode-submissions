class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force로 풀기 
        # 2개 pointer 비교해서 max_amount 값 업데이트하기 
        max_amount = 0
        for i in range(0,len(heights)-1):
            for j in range(i,len(heights)): 
                low,hgt = (j-i), min(heights[i],heights[j])

                if low > 0 and low*hgt > max_amount:
                    max_amount = low*hgt
        
        return max_amount 

"""
[2,2,2]

i = 0, j = 1 .. l = 1, h = 2, l*h=2=max_amount 
i = 0, j = 2 .. l = 2, h = 2, l*h=4=max_amount 

"""
                


        






""" 
 l             r
[1,7,2,5,4,7,3,6]
 0 1 2 3 4 5 6 7 

# 1) l과 j 중 작은 값 선정
# 2) 작은 값 * (idx[l]-idx[j])
# 3) max 값 업데이트 

"""