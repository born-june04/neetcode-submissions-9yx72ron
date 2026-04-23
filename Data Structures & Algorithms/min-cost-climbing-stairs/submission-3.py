class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost) ##i번째에서 떠나는 비용
        dp = [0]*(n+1) ##i번째까지 오는 비용

        for i in range(2, n+1):
            dp[i] = min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
        return dp[-1]