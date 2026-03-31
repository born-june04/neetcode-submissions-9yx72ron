class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sorted_nums = sorted(set(nums))

        n = len(sorted_nums)


        if n >= 1:
            count = 1
            max_count = 1

            for i in range(n-1):
                if abs(sorted_nums[i+1] - sorted_nums[i]) == 1:
                    count += 1
                else:
                    max_count = max(max_count, count)
                    count = 1
            
            max_count = max(max_count, count)
        else:
            max_count = 0
        
        return max_count