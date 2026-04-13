class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # i = 0, output[i] = 48, product of all of nums except nums[i] = 1, 1*|2*4*6
        # i = 1, output[i] = 24, product of all of nums except nums[i] = 2, 1*|4*6
        # i = 2, output[i] = 12, product of all of nums except nums[i] = 4, 1*2|*6
        # i = 3, output[i] = 8, product of all of nums except nums[i] = 6, 1*2*4|*1

        n = len(nums)
        prefix, suffix = [1]*n, [1]*n

        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i-1]

        for i in range(n-2, -1, -1):        
            suffix[i] = suffix[i+1]*nums[i+1]

        return [x*y for x,y in zip(prefix,suffix)]
            
        