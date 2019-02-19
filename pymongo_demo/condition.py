import json

from pymongo import MongoClient, DESCENDING

client = MongoClient(host='127.0.0.1', port=27017)
db = client.demo
collection = db['movie']

# Using the $lt, $gt, $lte, and $gte Operators

# m_list = collection.find({'imdb_score': {'$gt': 7}})

# for m in m_list:
#     print(m)

# $ne, $in, $nin

# m_list = collection.find({'country': {'$ne': "USA"}})

# for m in m_list:
#     print(m)

m_list = collection.find({"country": {'$in': ["UK", "Australia"]}})

for m in m_list:
    print(m)
