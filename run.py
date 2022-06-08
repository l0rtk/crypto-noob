import tweepy
from pprint import pprint
import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

username = os.environ.get('USER')
password = os.environ.get('PASSWORD')


client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.ekdn2cn.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

# client = tweepy.Client('AAAAAAAAAAAAAAAAAAAAAM06SgEAAAAAkZPNYb1U5pH63EdCMuFl%2BhRahYY%3DmWFcsHOU3r1xWbpdIbdyrmI31SuFuifzWt7w0Xgm1E5zSdf9k2')


# req = client.search_recent_tweets(query='messi',max_results=10)

# pprint(req)
# # for tweet in tweets:
#     # print(tweet)