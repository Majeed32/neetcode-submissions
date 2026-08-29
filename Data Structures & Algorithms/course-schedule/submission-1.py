class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_map = defaultdict(list)
        prereq_count = [0]*numCourses
        for u, v in prerequisites:
            prereq_map[v].append(u)
            prereq_count[u] += 1
        queue = deque()
        taken = set()
        for idx, val in enumerate(prereq_count):
            if not val:
                queue.append(idx)
                taken.add(idx)
        while queue:
            node = queue.popleft()
            for nei in prereq_map[node]:
                prereq_count[nei] -= 1
                if not prereq_count[nei]:
                    queue.append(nei)
                    taken.add(nei)
        return len(taken) == numCourses
        