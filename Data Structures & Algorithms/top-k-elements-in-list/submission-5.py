class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # ans = {} ## O(n)
        # for num in nums: ## O(n)
        #     if num not in ans:
        #         ans[num] = 1
        #     else:
        #         ans[num] += 1
        
        # return sorted(ans, key=lambda x: ans[x], reverse=True)[:k] # O (m log m where m is uqnie number of nums)
        # Time Complexity : O(n log n)

        # from collections import Counter
        # import heapq
        # count = Counter(nums)
        # heap = []

        # for num,freq in count.items(): # O(n)
        #     heapq.heappush(heap, (freq,num)) ## O(log k)
        #     if len(heap) > k:
        #         heapq.heappop(heap) ## O(log k)
        
        # return [num for freq, num in heap] # O(log n)
        # Time Complexity : O(n log k)

        from collections import Counter
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)] #[freq[num]]

        for num, freq in count.items():
            bucket[freq].append(num)
        
        ans = []
        for i in range(len(bucket)-1,0,-1):
            ans.extend(bucket[i])
            if len(ans) >= k:
                return ans[:k]
        # Time Complexity : O(n) for-loop
        