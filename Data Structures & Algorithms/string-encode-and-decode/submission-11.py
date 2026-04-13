class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded_string  = []
        for s in strs:
            length = len(s)
            encoded_string.append(f"{length}#{s}")
            
        return "".join(encoded_string);

    def decode(self, s: str) -> List[str]:
        
        strs = []
        i=0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            strs.append(word)
            i = j+1+length

        return strs

