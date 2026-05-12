class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # time O(n) 배열만큼 while문 도니까 
        # space O(1)
        max_area = 0 
        s, e = 0, len(heights)-1 

        while s < e: 
            hgt = min(heights[s], heights[e])
            area = (e-s)*hgt
            if area > max_area: 
                max_area = area 
            
            if heights[s] < heights[e]: 
                s += 1
            else: 
                e -= 1

        return max_area

"""
아이디어: 높이가 더 작은 쪽이 한칸 이동을 하면 됨 
"""
                


        






""" 
 l             r
[1,7,2,5,4,7,3,6]
 0 1 2 3 4 5 6 7 

# 1) l과 j 중 작은 값 선정
# 2) 작은 값 * (idx[l]-idx[j])
# 3) max 값 업데이트 

"""