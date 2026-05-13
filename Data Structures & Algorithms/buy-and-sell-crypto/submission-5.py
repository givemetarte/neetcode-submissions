class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 아이디어: 현 시점에서 이전 과거의 min 찾아서 계산 
        max_profit = 0 
        min_price = prices[0]

        for price in prices: 
            max_profit = max(max_profit, price - min_profit)
            min_price = min(min_price, price)

        return max_profit

# [10, 1, 5, 6, 7, 1]
#  ^: max_profit = 0, min_price = 10 
#      ^: max_profit = 0, min_price = 1 
#         ^: max_profit = 5, min_price = 1 
