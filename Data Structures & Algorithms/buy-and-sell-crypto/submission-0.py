class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy, sell moves as two pointer
        # buy <= sell
        # price[buy] < price[sell] -> profit
        # price[buy] >= price[sell] -> not profit, have to move
        # sell always move to right
        # buy moves when not profit

        n = len(prices)
        profit = 0

        left, right = 0,1

        while right < n:
            if prices[left] < prices[right]:
                profit = max(profit, prices[right] - prices[left])
            else:
                left = right
            
            right += 1

        return profit