class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # nums[i] + nums[j] and then use 0 to target specific number for nums[k]

        n = len(nums)
        output = []
        nums = sorted(nums)
        search = {k:v for k,v in zip(nums, range(n))}

        for i in range(n):
            for j in range(i+1,n):
                first_num = nums[i]
                second_num = nums[j]
                target = int(0 - (first_num + second_num))
                if target in nums:
                    if search[target] != i and search[target] != j:
                        comb = sorted([first_num, second_num, target])
                        if comb not in output:
                            output.append(comb)
        
        return output