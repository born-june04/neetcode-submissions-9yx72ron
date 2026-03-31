class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ## rec area = bar forms the rec

        stack = []
        area = 0

        for i,h in enumerate(heights):
            start = i
            while stack and h < stack[-1][-1]:
                idx, height = stack.pop()
                area = max(area, height * (i - idx))
                start = idx
            
            stack.append([start,h])
        
        while stack:
            idx, height = stack.pop()
            area = max(area, height * (len(heights) - idx))
        
        return area