class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        heap = [-x for x in nums]
        heapq.heapify(heap) ##[-5,-4,-3,-2,-1]

        for _ in range(k-1):
            heapq.heappop(heap)
        
        return -heap[0]
