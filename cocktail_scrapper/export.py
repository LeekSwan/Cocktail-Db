from pymongo import MongoClient
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()
CONNECTION_STRING = os.getenv('CONNECTION_STRING')
    
client = MongoClient(CONNECTION_STRING)
db = client["sample_airbnb"]
col = db["listingsAndReviews"]

mydoc = col.find_one({ "_id": "10006546"})
print(mydoc)

# # Issue the serverStatus command and print the results
# serverStatusResult=db.command("serverStatus")
# pprint(serverStatusResult)