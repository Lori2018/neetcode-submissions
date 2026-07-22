import heapq
from collections import defaultdict

class Twitter:
    # each user has an array of tweets ordered oldest to newest
    # only need length of 10 

    # hash map of users 
    # when a tweet is posted, add all 

    def __init__(self):
        # key = user, value = list of who user follows
        self.follows = defaultdict(set)
        # key = user, value = 10 most recent tweets 
        self.tweets = defaultdict(list) 
        # key = user, value = newsfeeds heaps
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if len(self.tweets[userId]) == 10:
            self.tweets[userId] = self.tweets[userId][1:]
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.tweets[userId].copy()
        # print(f"user: {userId}, tweets: {feed}")
        for user in self.follows[userId]:
            feed.extend(self.tweets[user])
        heapq.heapify(feed)
        feed = sorted(feed)
        res = [x[1] for x in feed][::-1]
        return res[:10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # insert into heap 
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId or followeeId not in self.follows[followerId]:
            return
        self.follows[followerId].remove(followeeId)
