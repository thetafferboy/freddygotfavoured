import json
import random
import tweepy
import string
import time
from random import randint

print ('==========================')
print ('Freddy Got Favoured')
print ('By @thetafferboy')
print ('==========================')

def run_freddy():

    #######################################################################################
    # Stuff for you to fill in:

    # Twitter API details:
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''

    # List of users that you want to use as seed accounts - the more the better
    users = ["thetafferboy", "googleanalytics"]
	
    #######################################################################################
 

    limit = len(users) - 1
    selected_user = users[randint(0,limit)]

    # Setup tweepy instance
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    print("Choosing liked tweet from: " + selected_user)

    for page in tweepy.Cursor(api.favorites, id=selected_user, wait_on_rate_limit=True, count=10).pages(1):
        choose_tweet = randint(0, 9)
        up_to_tweet = 0
        print ("Choosing tweet #"+str(choose_tweet))

        for status in page:
            up_to_tweet += 1

            if (up_to_tweet == choose_tweet):
                try:
                    print ("Adding fave: " + str(status.id))
                    api.create_favorite(status.id)
                except:
                    print ("Failed")

run_freddy()
