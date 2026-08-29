class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = defaultdict(list)
        prereq_count = [0]*numCourses
        for u, v in prerequisites:
            prereq_map[v].append(u)
            prereq_count[u] += 1
        queue = deque([i for i in range(numCourses) if prereq_count[i] == 0])
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for nei in prereq_map[node]:
                prereq_count[nei] -= 1
                if not prereq_count[nei]:
                    queue.append(nei)
        return res if len(res) == numCourses else []
        