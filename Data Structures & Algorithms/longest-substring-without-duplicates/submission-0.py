class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if the next one is not same as current -> update substring
        # if the next one is same or have seen before -> end substring and start compare

        n = len(s)
        seen = set()
        left = 0
        ans = 0

        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            ans = max(ans, right-left+1)
            
        return ans
