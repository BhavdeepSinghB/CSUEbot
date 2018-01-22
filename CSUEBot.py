import tweepy

CONSUMER_KEY = """JtJrYE0xXpwjniauniN9LBpBZ"""
CONSUMER_SECRET = """QdSha6pNCqweycD6MxqOJPlBJPFL2xQ0t02buXW41l0Y7BSHJE"""
ACCESS_KEY = '955224238473994240-ibyXcdbHR7KfNKE3gYWDbaxQK1Pm2H7'
ACCESS_SECRET = 'rCgWtXCNnyWyzUdyKJjBftDJhPHkK3j9Nm4kmR2Rmru5F'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

names = api.search_users("#CSUEB")

filename = "UsersToFollow.txt"
file = open(filename, "r")

for auser in names:
    api.create_friendship(file.readline())

file.close()

        