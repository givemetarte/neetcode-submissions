class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1

        while start < end: 
            mid = (start + end) // 2 
            if nums[mid] == target: 
                return mid 
            elif nums[mid] < target: 
               start += 1
            else: 
                end -= 1 
        
        return -1 

"""
      s e 
[-1,0,2,4,6,8]

mid = 5 // 2 = 2
mid = (1+5) // 2 = 3
mid = (1+4) // 2 = 2
mid = (2+4) // 2 = 3
mid = (2+3) // 2 = 2


"""
            
