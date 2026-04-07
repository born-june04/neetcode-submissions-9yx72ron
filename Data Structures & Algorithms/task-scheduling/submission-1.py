class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter, deque
        import heapq

        count = Counter(tasks)
        heap = [-x for x in count.values()]
        heapq.heapify(heap)

        queue = deque() ## cnt, remaining time
        time = 0

        while heap or queue:
            time += 1

            if heap:
                cnt = heapq.heappop(heap) + 1
                if cnt:
                    queue.append((cnt, time+n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

        return time

