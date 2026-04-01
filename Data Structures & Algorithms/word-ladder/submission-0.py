class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS
        
        from collections import deque

        wordSet = set(wordList) # O(1)
        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, dist = queue.popleft()
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i+1:]
                    if newWord in wordSet:
                        if newWord == endWord :
                            return dist + 1
                        if newWord not in visited:
                            visited.add(newWord)
                            queue.append((newWord, dist+1))
                    
        return 0
