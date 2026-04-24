class KthLargest:
    import heapq

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap) ## 부모 <= 자식
        while len(self.heap) > k: ## min heap에서 k개로 개수를 유지함
            heapq.heappop(self.heap) ## 0이 항상 k번째 작은 수 유지

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
        
