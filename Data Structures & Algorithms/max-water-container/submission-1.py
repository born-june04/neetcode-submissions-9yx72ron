class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area = width * height
        # width = (j-i) where j > i
        # height = min(height[i], height[j])

        n = len(heights)
        area = 0

        # for i in range(n-1):
        #     for j in range(i,n):
        #         width = j - i
        #         height = min(heights[i], heights[j])
        #         area = max(width*height, area)
        
        # return area

        left, right = 0, n-1
        while left < right:

            area = max(area, (right - left) * min(heights[left], heights[right]))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return area