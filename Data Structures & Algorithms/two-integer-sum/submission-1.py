class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i,num in enumerate(nums):
            compare = target - num
            if compare in seen:
                return [seen[compare],i]
            else:
                seen[num] = i