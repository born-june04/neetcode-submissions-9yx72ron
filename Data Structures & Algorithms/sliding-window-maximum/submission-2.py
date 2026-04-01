class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        from collections import deque
        
        n = len(nums)
        if n <= 0:
            return nums

        dq = deque()
        ans = []

        for r in range(n):
            # 현재값보다 작은 건 뒤에서 제거
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()
            dq.append(r)

            # winodw 밖으로 나간 인덱스 제거
            if dq[0] < r-k+1:
                dq.popleft()

            # window 크기 됐으면 최댓값 추가
            if r >= k-1:
                ans.append(nums[dq[0]])
        
        return ans
