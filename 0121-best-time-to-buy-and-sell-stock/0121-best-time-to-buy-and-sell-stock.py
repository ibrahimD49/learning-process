class Solution:
    def maxProfit(self, p: List[int]) -> int:
        min_price = p[0]
        max_price = 0

        for price in p:
            min_price = min(min_price,price)
            max_price = max(max_price,price - min_price)
            
        return max_price
                







        