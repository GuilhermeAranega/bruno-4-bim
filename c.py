import pymongo
import hashlib
 
client = pymongo.MongoClient("mongodb://localhost:27017/banco")
db = client["banco"]

string = input("string: ")
hashString = hashlib.sha256(string.encode())

db["documento"].insert_one({
    "hash": hashString.hexdigest()
})

