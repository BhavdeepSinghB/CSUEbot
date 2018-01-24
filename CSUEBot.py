import tweepy

CONSUMER_KEY = #
CONSUMER_SECRET = #
ACCESS_KEY = #
ACCESS_SECRET = #

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = "Users2.txt"
fw = open(filename, "a")
fr = open(filename, "r")

count = 0
while(count < 5):
    names = api.search_users("CSUEB", 20, count)
    for auser in names:
        fw.write("%s\n" % auser.screen_name)
    for anotheruser in names:
        api.create_friendship(fr.readline())
    count = count + 1
    print ("Number of pages covered %s" % count)
    time.sleep(600)

'''while(count <= 100):
    api.destroy_friendship(fr.readline())
    count = count + 1
'''

fw.close()
fr.close()
        
