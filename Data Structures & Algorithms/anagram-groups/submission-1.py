class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}
        for s in strs:
            sorted_s = "".join(sorted(s)) ## why sorted? -> [cat] will become alphabetic order [act]
            if sorted_s not in seen:
                seen[sorted_s] = [s]
            else:
                seen[sorted_s].append(s)

        return list(seen.values())

