class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        # generate map
        s_dict = {}
        for i in s:
            if i not in s_dict:
                s_dict[i] = 1
            else:
                s_dict[i] += 1
        
        # compare with t
        for i in t:
            if i in s_dict:
                s_dict[i] -= 1
        
        return all(v == 0 for v in s_dict.values())