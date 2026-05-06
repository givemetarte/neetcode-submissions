class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf') # 최소 매수가격 (무한대로 초기화)
        max_profit = 0 # 최대 이익 (초기값 0)

        for price in prices:
            # 최소 매수가격이 더 작게 업데이트
            if min_price > price:
                min_price = price

            # 손익계산
            profit = price - min_price
            max_profit = max(max_profit, profit) # 최대 이익갱신
        
        return max_profit
            