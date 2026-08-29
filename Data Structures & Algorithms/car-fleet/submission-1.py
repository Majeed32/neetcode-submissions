class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(position[i], speed[i]) for i in range(len(position))]
        pair.sort(reverse=True)
        res = 0
        curr = 0
        for p, s in pair:
            t = (target - p)/s
            if t > curr:
                res += 1
                curr = t
        return res
        