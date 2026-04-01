class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_count = {}
        for c in s1:
            s1_count[c] = s1_count.get(c,0) + 1
        
        window = {}
        n1,n2 = len(s1),len(s2)

        for r in range(n2):
            window[s2[r]] = window.get(s2[r],0) + 1

            # window 크기가 s1보다 크면 왼쪽 제거
            if r >= n1:
                left_char = s2[r-n1]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
            
            if window == s1_count:
                return True
        
        return False
