import json

from pymongo import MongoClient, DESCENDING

client = MongoClient(host='127.0.0.1', port=27017)
db = client.demo
collection = db['test']

# insert some test data

# collection.insert_many(
#     [
#         {"x": 1, "y": 1},
#         {"x": 2, "y": 2},
#         {"x": 3, "y": 3},
#         {"x": 4, "y": 4},
#         {"x": 5, "y": 5}
#     ]
# )
