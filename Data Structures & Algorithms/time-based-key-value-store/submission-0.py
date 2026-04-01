class TimeMap:

    def __init__(self):
        self.store = {} # {key: [(ts, val)]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
    
        pairs = self.store[key]
        l, r = 0, len(pairs)-1
        ans = ""

        while l<=r:
            mid = (l+r)//2
            if pairs[mid][0] <= timestamp:
                ans = pairs[mid][1] # 후보저장
                l = mid+1 # 더 최근 거 있는지 확인
            else:
                r = mid-1
        
        return ans
        
