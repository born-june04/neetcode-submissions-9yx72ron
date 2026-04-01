class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = -heapq.heappop(heap) # max weights
            second = -heapq.heappop(heap)

            if first != second:
                heapq.heappush(heap, -(first-second))
        
        return -heap[0] if heap else 0