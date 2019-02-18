import json

from pymongo import MongoClient, DESCENDING

client = MongoClient(host='127.0.0.1', port=27017)
db = client.demo
collection = db['movie']

# m = collection.find_one({'title_year': 2020})
# print(m)

# for m in collection.find({'title_year': 2015}, projection={"_id": False, "title": True, "director_name": True}):
#     print(m)

"""

a = {
    "a": {"key": 1},
    "b": 1
}

b = {
    "a": {"key":2}
}

c = {
    "a": {"key": 1, "v":2}
}

collection.find({'a.key': 1})

"""


# sort, limit, skip

# for m in collection.find(
#     projection={"_id": False, "title": True, "imdb_score": True}).sort("imdb_score", DESCENDING).skip(20).limit(10):
#     print(m)


# count , distinct

print(collection.find({"title_year": 2015}).count())


print(len((collection.find().distinct('director_name'))))


