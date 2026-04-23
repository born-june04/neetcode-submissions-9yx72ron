class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # holding = 주식 들고 있음
        # sold = 방금 팔았음, 내일 cooldown
        # cooldown = 쉬는 날, 내일 살 수 있음

        # holding, sold, cooldown = float('-inf'),0,0

        # for price in prices:
        #     prev_holding = holding
        #     prev_sold = sold
        #     prev_cooldown = cooldown

        #     holding = max(prev_holding, prev_cooldown - price) #들고있거나 새로 사거나
        #     sold = prev_holding + price # 오늘 팔기
        #     cooldown = max(prev_cooldown, prev_sold) #쉬거나 어제 판 상태
        
        # return max(sold, cooldown)

        n = len(prices)

        dp = [[0]*3 for _ in range(n+1)] ## holding, sold, cooldown
        dp[0][0] = float('-inf')

        for i in range(1,n+1):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i-1]) ## holding
            dp[i][1] = dp[i-1][0]+prices[i-1]
            dp[i][2] = max(dp[i-1][1], dp[i-1][2])
        
        return max(dp[n][1], dp[n][2])