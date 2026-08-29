class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adjList = defaultdict(list)
        queue = deque([[beginWord, 1]])
        seen = {beginWord}
        n = len(beginWord)
        for word in wordList:
            for i in range(n):
                wildcard = word[ : i] + '*' + word[i+1 : ]
                adjList[wildcard].append(word)
        
        while queue:
            curr, num_of_words = queue.popleft()
            if curr == endWord:
                return num_of_words
            for i in range(len(curr)):
                wildcard = curr[ : i] + '*' + curr[i+1 : ]
                for word in adjList[wildcard]:
                    if word not in seen:
                        queue.append([word, num_of_words+1])
                        seen.add(word)
        return 0
        
        