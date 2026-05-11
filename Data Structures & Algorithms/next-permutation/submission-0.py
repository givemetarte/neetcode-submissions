class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # 최대 순열이 아닐 때까지 오른쪽에서 왼쪽으로 한칸씩 이동 
        low = len(nums)-2
        while 0 <= low and nums[low] >= nums[low+1]:
            low -= 1 
        
        # 범위에서 가장 좌측에 있는 숫자보다 가장 근소하게 큰 값을 우측에서 찾아서 자리를 바꿔줌
        if low > -1: 
            high = len(nums)-1 
            while 0 <= high and nums[low] >= nums[high]: 
                high -= 1
            nums[low], nums[high] = nums[high], nums[low]
        
        # 자리를 바꾼 좌측 숫자 다음에 있는 모든 숫자를 역순으로 재배열 
        start, end = low+1, len(nums)-1 
        while start < end: 
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start+1, end-1

