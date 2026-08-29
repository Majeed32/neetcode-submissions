class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wild_map = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                wildcard = word[ : i] + "*" + word[i+1 :]
                wild_map[wildcard].append(word)
        queue = deque([beginWord])
        seen = {beginWord}
        word_count = 0
        while queue:
            word_count += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == endWord:
                    return word_count
                for i in range(len(node)):
                    wildcard = node[ : i] + "*" + node[i+1 : ]
                    for word in wild_map[wildcard]:
                        if word not in seen:
                            seen.add(word)
                            queue.append(word)
        return 0


        