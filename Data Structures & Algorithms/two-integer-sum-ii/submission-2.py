class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l,r,n = 0,1,len(numbers)


        while l < n:
            lc,lr = numbers[l],numbers[r]
            
            if lc+lr == target:
                return [l+1,r+1]
            
            if r == n-1:
                r = 1
                l += 1
            else:
                r += 1
        
