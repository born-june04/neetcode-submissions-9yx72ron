class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # using the window to navitagte
        # condition 1, if the ch in s also in t?
        # if not, move to next
        # if yes, extend to window
        # condition 2, when you've already found one, you can try to stretch the window until you find all t
        # condition 3, use minimum calculation to return the minimum substring in s

        left,right = 0,1
        n = len(s)

        need = {}
        for c in t:
            need[c] = need.get(c,0)+1
        required = len(need)
        
        have = {} # current ch count
        formed = 0
        ans = ""

        for right in range(n):

            if s[right] in need:
                have[s[right]] = have.get(s[right],0) + 1
                if have[s[right]] == need[s[right]]:
                    formed += 1

            while formed == required: ## when we all find the t in s
                if not ans or len(s[left:right+1]) < len(ans):
                    ans = s[left:right+1]
                
                if s[left] in have:
                    have[s[left]] -= 1 ##minimizing the window
                    if s[left] in need and have[s[left]] < need[s[left]]:
                        formed -= 1
                left += 1

        return ans