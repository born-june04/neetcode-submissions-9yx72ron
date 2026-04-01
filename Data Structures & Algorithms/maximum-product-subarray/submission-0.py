class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        ans = max(nums)
        cur_max = 1
        cur_min = 1

        for num in nums:
            if num == 0:
                cur_max = 1
                cur_min = 1
                continue
        
            temp = cur_max
            cur_max = max(num, cur_max*num, cur_min*num)
            cur_min = min(num, temp*num, cur_min*num)
            ans = max(ans, cur_max)
        
        return ans