"""

Data Structures for our OOD: 


# This handles the follow and following and unfollowing feature:
    userId -> Hashset of FolloweeID's ( HashSet is way better than using a list, hashset removal = O(1) and list removal is O(n)

# Posting of Tweet 
    userId -> [ TweetId ] ( will change! )

# getNewsFeed
- We need to fetch at most the 10 recent tweet ID's in the user's news feed, ech item must be posted by users who the user is following or by the user themselves 

- we need a list of pairs, we can use TIME, to attach to each post, so that we can use it with our tweetID


UserID -> list of a couple [ count, TweetID]





"""

from collections import defaultdict
class Twitter:

    def __init__(self):
        # this is used to keep track of the time in which a tweet was posted
        self.time = 0 

        # this is our hashMap that will map a user to a list of tweets that also contains the time it was posted
        self.tweetMap = defaultdict(list)

        # Maps users to the people they follow! a set makes removal quicker! 
        self.followMap = defaultdict(set)


        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time -= 1 


    
    def getNewsFeed(self, userId: int) -> List[int]:
        list_of_recent_tweets = [] # Ordered starting from recent 
        min_heap = [] # figures out the most recent! 

        # we just add ourselves to our followee and include our posts too
        self.followMap[userId].add(userId)

        # go through each followeeID, this goes through the most recent posts once 
        for followeeId in self.followMap[userId]:

            if followeeId in self.tweetMap: 


                # So no we need to go through each tweet the followee Created!

                # first retrieve the list of all tweets from followee 
                list_of_tweets_from_followee = self.tweetMap[followeeId]

                # retrieving the most recent tweet's positon
                index_of_most_recent_tweet = len(list_of_tweets_from_followee) - 1 

                #Now lets retrieve the actual values from the most recently posted tweet, we can do this by unpacking the couple (count, tweetId)
                count, tweetId = self.tweetMap[followeeId][index_of_most_recent_tweet]
                
                # 1. count is our key, thats how we will order them
                # 2. tweetId is just the tweet itself
                # 3. followeeId, helps us get the next position
                # 4. helps us get to the next index! 
                min_heap.append([count, tweetId, followeeId, index_of_most_recent_tweet - 1])  


        # Now we can order our heap using heapify
        heapq.heapify(min_heap)

        # once we've done our initial scan above which will fulfill if the user follows more than 10 people and assuming all those 10 people have posts

        # we still need to add aother potential most recent posts that the followers may have posted that not just include their most recent post! 

        while min_heap and len(list_of_recent_tweets) < 10: 
            # pop our max heap that gives out the most recent tweet
            count, tweetId, followeeId, index = heapq.heappop(min_heap)
            # pop that into our result
            list_of_recent_tweets.append(tweetId)
            if index >= 0:
                # count and tweetId are now given of the follower's next most recent post
                count, tweetId = self.tweetMap[followeeId][index]
                # we add to 
                heapq.heappush(min_heap, [count, tweetId, followeeId, index - 1])

        return list_of_recent_tweets 






        

    def follow(self, followerId: int, followeeId: int) -> None:

        # What if we already follow the user? We should let them know or error it out!
        if followeeId in self.followMap[followerId]: 
            return None 

        # Else we just add it to our set
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # If the followee exits then aand only then can we even unfollow a userID 
        if followeeId in self.followMap[followerId]: 
            self.followMap[followerId].remove(followeeId)
            



