class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 100  # 최소 가격
        max_profit = 0  # 최대 수익

        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price
            max_profit = max(max_profit, profit)
        
        return max_profit
            