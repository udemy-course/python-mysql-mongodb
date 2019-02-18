import json

from pymongo import MongoClient, DESCENDING

client = MongoClient(host='127.0.0.1', port=27017)
db = client.demo
collection = db['movie']

# Using the $lt, $gt, $lte, and $gte Operators

