class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_dict = {}
        for i in s:
            s_dict[i] = s_dict.get(i,0)+1

        for char in t:
            if char not in s_dict:
                return False
            s_dict[char] -= 1
            if s_dict[char] < 0:
                return False
        
        return all(count==0 for count in s_dict.values())