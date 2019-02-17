from pymongo import MongoClient

client = MongoClient(host='127.0.0.1', port=27017)

print(client.server_info())

# use demo

db = client.demo

print(db)

# collection = db.movie
collection = db['movie']

print(collection)

# data insert

# collection.insert_one(
#     {
#         "_id": '123456',
#         "A": [1, 2, 3 ],
#         "B": {
#             "X": 1,
#             "Y": 2,
#             "Z": 3
#         }
#     }
# )

collection.insert_many(
    [
        {
            "AA": 1,
            "BB": 2
        },
        {
            "AA": 12,
            "BB": 13
        }
    ]
)


