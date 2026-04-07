class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # nums[i] + nums[j] and then use 0 to target specific number for nums[k]
        # O(n^2)
        n = len(nums)
        output = []

        nums.sort()
        for i in range(n):
            if i> 0 and nums[i] == nums[i-1]:
                continue

            left, right = i+1, n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                comb  = [nums[i], nums[left], nums[right]]
                if total == 0:
                    output.append(comb)
                
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0: ## because we sorted
                    left += 1
                else:
                    right -= 1
        
        return output

