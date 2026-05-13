# 문제풀이2. heap으로 풀기 
from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums: 
            if len(heap) < k: 
                heappush(heap, num)
            else: 
                if heap[0] < num:
                    heappop(heap)
                    heappush(heap, num)
        return heap[0] 

"""
heap에 데이터 추가 시 time O(logk) 
heap의 가장 작은 값 또는 최소값 제거시 time O(1)
space O(k) (heap 원소 개수만큼 부여)

Q. heap이 자동으로 정렬되는 건가? 

[2,3,1,5,4] k=2 
여기에서 heap이 k개만큼 생성 

num = 2
heap: [2]

num = 3
heap: [2,3]

num = 1 
heap: [2,3] > 1이므로 pass 

num = 5
heap: [2,3] < 5이므로 heap[0]빼고 heap추가 

num = 4
heap: [3,5] > 4이므로 heap[0]빼고 heap추가
"""