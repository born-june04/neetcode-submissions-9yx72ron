class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # dp = [0]*n

        # def rob1(nums):
        #     dp1, dp2 = 0,0
        #     for n in nums:
        #         dp1, dp2 = dp2, max(dp2,dp1+n)
        #     return dp2
        
        # return max(rob1(nums[:-1]), rob1(nums[1:]))

        ## rob1과 다르게 이거는 원형
        def rob1(nums):
            n = len(nums)
            if n<=1:
                return nums[0]

            dp = [0]*n
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,n):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            return dp[-1]
        
        without_first_house = rob1(nums[1:])
        with_first_house = rob1(nums[:-1])
        return max(without_first_house, with_first_house)