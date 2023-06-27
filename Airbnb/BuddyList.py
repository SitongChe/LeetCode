#  /**
# * 我有一个感兴趣的城市wishlist，我的朋友们每个人也有感兴趣的城市wishlist,
# * 如果朋友和我感兴趣的城市占总共他总城市个数的至少一半，那么他就是你的buddy，相同城市越多，similarity越高
# *
# * 1. 按照similarity从高到低把你的buddy排序，输出名字及相同的城市
# * 2. 推荐k个城市，这些城市是不在你的wishlist的城市，从similarity高到低的buddy里面依次找
# *
# * Example
# * Your wishlist: a,b,c,d
# * Buddy1 wishlist: a,b,e,f  (有两个和你的一样，所以是你的buddy)
# * Buddy2 wishlist: a,c,d,g  (有三个和你的一样，也是你的buddy)
# *
# * - k = 10，buddy1和buddy2的wishlist中不在你的wishlist中的城市都可以加入推荐中，因为buddy2的重合度更高，
# *   所以先输出buddy2中的，所以推荐为 g,e,f
# * - k = 2，推荐是g,e 或 g,f
# */
from typing import List, Dict
class RecommendationSystem:
    def findBuddiesAndRecommendations(self,your_wishlist: List[str], friends_wishlists: Dict[str, List[str]], k: int) -> List[str]:
        mylistSet = set(your_wishlist)
        mylistCount = len(mylistSet)
        buddies = []
        # build buddy list
        for friend,wishlist in friends_wishlists.items():
            overlap = len(mylistSet.intersection(set(wishlist)))
            if overlap>=mylistCount//2:
                buddies.append([friend,overlap])
        #sort by similarity
        buddies.sort(key = lambda x:x[1], reverse=True)
        #output result
        print("your wishlist:", your_wishlist)
        for i,buddy in enumerate(buddies):
            print(buddy[0]," wishlist: ",friends_wishlists[buddy[0]])
        #build recommendation
        recommendation = {}
        for i,buddy in enumerate(buddies):
            for city in friends_wishlists[buddy[0]]:
                if city not in mylistSet:
                    cnt = 1
                    index = i
                    if city in recommendation:
                        cnt =recommendation[city][0]+1
                        index = min(index, recommendation[city][1])
                    recommendation[city]=[cnt,index]
                    
        # sort recommendation by count (reverse) and buddy rank (ascending)
        ans = sorted(recommendation.items(), key=lambda x: (-x[1][0], x[1][1]))
       
        return [city for city, _ in ans[:k]]
        
            
# Test the code
rs = RecommendationSystem()
your_wishlist =["a","b","c","d"]
friends_wishlists = {
    'Buddy1': ['a', 'b', 'e', 'f'],
    'Buddy2': ['a', 'c', 'd', 'g'],
    'Buddy3': ['a', 'b', 'l', 'f'],
}
ans = rs.findBuddiesAndRecommendations(your_wishlist, friends_wishlists, 10)
print("recommendation: ",ans)
