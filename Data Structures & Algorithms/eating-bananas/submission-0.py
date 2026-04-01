class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        left, right = 1, max(piles)
        ans = right

        while left <= right:
            mid = (left+right)//2
            time = sum(math.ceil(pile/mid) for pile in piles)

            if time <= h: # 충분히 빠름, 더 느리게 가능
                ans = mid
                right = mid-1
            else:
                left = mid+1 
        
        return ans