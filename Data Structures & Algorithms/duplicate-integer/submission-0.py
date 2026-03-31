class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # n = len(nums)
        # ans = False

        # for i in range(n):
        #     first_num = nums[i]
        #     ref_nums = nums[i+1:]

        #     if first_num in ref_nums:
        #         ans = True
        
        # return ans

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        
        return False