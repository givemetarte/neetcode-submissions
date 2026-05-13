class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        start, end = 0, len(prices)-1

        while start < end:
            if (prices[end]-prices[start]) > answer:
                answer = prices[end]-prices[start]
            start += 1
            end -= 1
        
        return answer