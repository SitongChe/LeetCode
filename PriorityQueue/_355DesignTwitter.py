#https://leetcode.com/problems/design-twitter/
#time getNewsFeed O(f*logm) space O(m+f)  m:tweets  f:followees; others O(1)
class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweets[userId].append((self.time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        ans = []
        maxHeap = []
        self.following[userId].add(userId)
        for followeeId in self.following[userId]:
            if followeeId in self.tweets and self.tweets[followeeId]:
                index = len(self.tweets[followeeId])-1
                time,tweetId = self.tweets[followeeId][index]
                heapq.heappush(maxHeap,(-time,tweetId,followeeId,index-1))
        for i in range(10):
            if not maxHeap:
                return ans
            time,tweetId,followeeId,index = heapq.heappop(maxHeap)
            ans.append(tweetId)
            if index>=0:
                time,tweetId = self.tweets[followeeId][index]
                heapq.heappush(maxHeap,(-time,tweetId,followeeId,index-1))
        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
    

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following and followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
