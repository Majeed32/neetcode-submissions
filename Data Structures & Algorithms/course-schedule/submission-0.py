class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = {}
        for i in range(numCourses):
            indegree[i] = 0
        for course, pre in  prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        queue = deque([i for i in indegree if indegree[i] == 0])
        visited = set()
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                visited.add(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
        return len(visited) == numCourses
        