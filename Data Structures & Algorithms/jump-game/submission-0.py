class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        max_reach = 0 ## 현재까지 도달 가능한 최대 인덱스

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i+nums[i])
        
        return True