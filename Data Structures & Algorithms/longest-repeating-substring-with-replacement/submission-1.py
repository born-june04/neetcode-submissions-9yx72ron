class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        # compute each chunk of numbers
        # 1X2Y1X or 3A1B1A2B
        # use k value to replace each to get max substring length

        count = {}
        n = len(s)
        left = 0
        ans = 0

        for right in range(n):
            if s[right] not in count:
                count[s[right]] = 1
            else:
                count[s[right]] += 1

            # window size - most count > k
            while (right-left+1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1
            
            ans = max(ans, right-left+1)
        
        return ans
