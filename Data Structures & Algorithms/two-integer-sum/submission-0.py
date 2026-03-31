class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # n = len(nums)
        # ref = {k:v for k,v in zip(nums,range(len(nums)))}
        # ans = [0]*2

        # for num in nums:
        #     compare_num = target - num
        #     if compare_num in ref.keys():
        #         ind_1, ind_2 = ref[num], ref[compare_num]
        #         ans[0] = min(ind_1, ind_2)
        #         ans[1] = max(ind_1, ind_2)
        

        # return ans

        seen = {}

        for i, num in enumerate(nums):
            compare = target - num

            if compare in seen:
                return [seen[compare], i]
            
            seen[num] = i