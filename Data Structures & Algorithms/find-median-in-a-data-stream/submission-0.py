class MedianFinder:

    def __init__(self):
        self.small = [] ## max heap (음수로 저장)
        self.large = [] ## min heap

    def addNum(self, num: int) -> None:
        # small에 먼저 push
        heapq.heappush(self.small, -num)

        # small 최댓값이 large 최솟값보다 크면 교환
        if self.small and self.large \
        and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))
        
        # 크기 균형 유지
        if len(self.small) > len(self.large)+1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
        
        