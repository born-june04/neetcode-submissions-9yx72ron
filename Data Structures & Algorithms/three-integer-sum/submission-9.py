class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # nums[i] + nums[j] and then use 0 to target specific number for nums[k]

        n = len(nums)
        output = []
        # nums = sorted(nums)
        # search = {k:v for k,v in zip(nums, range(n))}

        # for i in range(n):
        #     for j in range(i+1,n):
        #         first_num = nums[i]
        #         second_num = nums[j]
        #         target = int(0 - (first_num + second_num))
        #         if target in nums:
        #             if search[target] != i and search[target] != j:
        #                 comb = sorted([first_num, second_num, target])
        #                 if comb not in output:
        #                     output.append(comb)
        
        # return output

        nums.sort()
        for i in range(n):
            left, right = i+1, n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                comb  = [nums[i], nums[left], nums[right]]
                if total == 0 and comb not in output:
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