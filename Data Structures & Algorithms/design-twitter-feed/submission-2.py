class Twitter:

    def __init__(self):
        self.posts = defaultdict(list)
        self._follow = defaultdict(set)
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((-self.time, tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = [pair for pair in self.posts[userId]]
        for nei in self._follow[userId]:
            heap.extend(self.posts[nei])
        heapq.heapify(heap)
        res = []
        while heap and len(res) < 10:
            t, id = heapq.heappop(heap)
            res.append(id)
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self._follow[followerId].add(followeeId)
        
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self._follow[followerId].discard(followeeId)
        
