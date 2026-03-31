class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ans = {}
        for num in nums:
            if num not in ans:
                ans[num] = 1
            else:
                ans[num] += 1
        
        return sorted(ans, key=lambda x: ans[x], reverse=True)[:k]