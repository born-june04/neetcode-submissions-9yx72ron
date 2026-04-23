class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp = [0]*n

        def rob1(nums):
            dp1, dp2 = 0,0
            for n in nums:
                dp1, dp2 = dp2, max(dp2,dp1+n)
            return dp2
        
        return max(rob1(nums[:-1]), rob1(nums[1:]))