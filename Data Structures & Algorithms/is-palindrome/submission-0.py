class Solution:
    def isPalindrome(self, s: str) -> bool:

        forward_s = "".join(c.lower() for c in s if c.isalnum())
        return forward_s == forward_s[::-1]


        
            
        