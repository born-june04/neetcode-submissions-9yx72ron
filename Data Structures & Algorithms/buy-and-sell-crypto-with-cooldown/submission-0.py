class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        holding, sold, cooldown = float('-inf'),0,0

        for price in prices:
            prev_holding = holding
            prev_sold = sold
            prev_cooldown = cooldown

            holding = max(prev_holding, prev_cooldown - price)
            sold = prev_holding + price
            cooldown = max(prev_cooldown, prev_sold)
        
        return max(sold, cooldown)