class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adjList = defaultdict(list)
        for u, v, p in flights:
            adjList[u].append([v, p])
        min_cost = {}
        min_cost[(src, 0)] =  0
        heap = [[0, 0, src]]
        while heap:
            price, stops, node = heapq.heappop(heap)
            if node == dst and stops <= k + 1:
                return price
            if stops <= k:
                for neighbor, p in adjList[node]:
                    new_price = p + price
                    if new_price < min_cost.get((neighbor, stops + 1), float("inf")):
                        min_cost[(neighbor, stops+1)] = new_price
                        heapq.heappush(heap, [new_price, stops + 1, neighbor])
        return -1