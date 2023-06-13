#https://leetcode.com/problems/design-twitter/
#time getNewsFeed O(f*logm) space O(m+f)  m:tweets  f:followees; others O(1)
class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time +=1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        ans = []
        self.followMap[userId].add(userId)
        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                index = len(self.tweetMap[followee])-1
                time, tweetId = self.tweetMap[followee][index]
                heapq.heappush(maxHeap,[-time,index,tweetId,followee])
        for i in range(10):
            if not maxHeap:
                return ans
            time,index,tweetId,followee = heapq.heappop(maxHeap)
            ans.append(tweetId)
            if index >0:
                time,tweetId=self.tweetMap[followee][index-1]
                heapq.heappush(maxHeap,[-time,index-1,tweetId,followee])
        
        return ans
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
