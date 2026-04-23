class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2

        dp = [False] * (target + 1) ## 지금까지 본 숫자들 중 일부를 골라서 합계 j를 만들 수 있다
        dp[0] = True

        for num in nums:
            for j in range(target, num-1, -1): # backward
                dp[j] = dp[j] or dp[j-num] ## j,0 or j,num으로 생성
        
        return dp[target]