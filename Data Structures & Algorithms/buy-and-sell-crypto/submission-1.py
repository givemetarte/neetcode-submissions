class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = []
        start, end = 0, len(prices)-1

        while start < end:
            p = prices[end]-prices[start]
            if p < 0:
                answer.append(0)
            else: answer.append(p)
            start += 1
            end -= 1
        
        return max(answer)