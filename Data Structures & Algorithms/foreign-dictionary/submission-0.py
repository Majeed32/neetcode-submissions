class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_list = {char: set() for word in words for char in word}
        indegree = {char : 0 for char in adj_list}
        for i in range(len(words)-1):
            first, second = words[i], words[i+1]
            min_length = min(len(first), len(second))
            if len(first) > min_length and first[ : min_length] == second[ : min_length]:
                return ""
            for i in range(min_length):
                if first[i] != second[i]:
                    if second[i] not in adj_list[first[i]]:
                        adj_list[first[i]].add(second[i])
                        indegree[second[i]] += 1
                    break
        queue = deque([char for char in indegree if not indegree[char]])
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for nei in adj_list[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return "" if len(res) != len(indegree) else "".join(res)
        