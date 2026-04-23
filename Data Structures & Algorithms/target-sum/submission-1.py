class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # dp = {0:1}

        # for num in nums:
        #     next_dp = {}
        #     for total,count in dp.items():
        #         next_dp[total+num] = next_dp.get(total+num,0)+count
        #         next_dp[total-num] = next_dp.get(total-num,0)+count
        #     dp = next_dp
        
        # return dp.get(target, 0)

        from functools import lru_cache
        @lru_cache(maxsize=None)

        def dfs(i, total):
            if i == len(nums):
                return 1 if total == 0 else 0
            return dfs(i+1, total-nums[i]) + dfs(i+1, total+nums[i])
        return dfs(0, target)

