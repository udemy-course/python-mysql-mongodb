from pymongo import MongoClient

client = MongoClient(host='127.0.0.1', port=27017)
db = client.demo
collection = db['movie']

with open('movie.json') as f:
    movie_list = json.load(f)
    collection.insert_many(movie_list)

client.close()
