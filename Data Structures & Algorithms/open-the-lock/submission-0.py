class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque([('0000', 0)])
        visited = set(deadends)
        if '0000' in visited: return -1
        visited.add('0000')
        while q:
            curr, steps = q.popleft()
            if curr == target:
                return steps
            
            for i in range(4):
                num = (int(curr[i]) + 1) % 10
                back = (int(curr[i]) -1) % 10
                
                new_curr = curr[:i] + str(num) + curr[i+1:]
                if new_curr not in visited:
                    visited.add(new_curr)
                    q.append((new_curr,steps+1))

                new_back = curr[:i] + str(back) + curr[i+1:]
                if new_back not in visited:
                    visited.add(new_back)
                    q.append((new_back,steps+1))
        
        return -1
                