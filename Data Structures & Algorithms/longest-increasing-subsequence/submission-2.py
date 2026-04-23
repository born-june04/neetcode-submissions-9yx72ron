class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)

        dp = [1]*n ## nums[i]로 하는 최대 길이

        for i in range(1,n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1) # 지금 방법으로 갈꺼냐, 아니면 subsequence까지 세서 갈꺼냐
        
        return max(dp)