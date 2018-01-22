import tweepy

CONSUMER_KEY = #
CONSUMER_SECRET = #
ACCESS_KEY = #
ACCESS_SECRET = #

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

names = api.search_users("#CSUEB")

filename = "UsersToFollow.txt"
file = open(filename, "r")

for auser in names:
    api.create_friendship(file.readline())

file.close()

        