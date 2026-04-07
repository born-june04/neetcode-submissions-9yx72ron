class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} ## key -> node

        self.left = Node() ## LRU 쪽 가장 오래됨
        self.right = Node() ## MRU 쪽 가장 최근
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        prev,next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def insert(self, node): # 항상 right 바로 옆에 삽입 (최근사용)
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key]) # 최근 사용으로 업데이트
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            lru = self.left.next # 가장 오래된 노드
            self.remove(lru)
            del self.cache[lru.key]
        
