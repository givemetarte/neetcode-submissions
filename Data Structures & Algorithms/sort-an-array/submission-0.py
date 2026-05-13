class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 1개 원소인 경우 종료 
        if len(nums) <= 1: return nums 

        # pivot 설정 
        pivot = nums[0]
        tail = nums[1:]

        # pivot 기준으로 왼쪽 오른쪽 tail 생성 
        left_tail = [i for i in tail if i <= pivot]
        right_tail = [i for i in tail if i > pivot]

        return self.sortArray(left_tail) + [pivot] + self.sortArray(right_tail)

