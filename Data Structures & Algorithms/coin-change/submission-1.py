class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)

        dp = [float('inf')]*(amount+1) ## i원 만들기 저장
        dp[0] = 0

        for target in range(1, amount + 1):
            for coin in coins:
                if target >= coin:
                    dp[target] = min(dp[target], dp[target-coin]+1)
        
        return dp[amount] if dp[amount] != float('inf') else -1