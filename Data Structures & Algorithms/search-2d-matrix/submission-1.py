class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows-1
        target_r, target_c = None, None

        while top <= bot:
            mid_r = (top+bot)//2
            if target < matrix[mid_r][0]: ## 요 부분을 헷갈려함
                bot = mid_r-1
            elif target > matrix[mid_r][-1]:
                top = mid_r+1
            else:
                target_r = mid_r
                break
        
        
        left, right = 0, cols-1

        while left <= right:
            if target_r is None:
                return False
            mid_c = (left+right)//2
            if target < matrix[target_r][mid_c]:
                right = mid_c-1
            elif target > matrix[target_r][mid_c]:
                left = mid_c+1
            else:
                target_c = mid_c
                break
        
        return target_c is not None