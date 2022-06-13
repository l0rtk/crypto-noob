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

