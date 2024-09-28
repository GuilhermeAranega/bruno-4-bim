import pymongo
import hashlib
 
client = pymongo.MongoClient("mongodb://localhost:27017/banco")
db = client["banco"]

string = input("string: ")
hashString = hashlib.sha256(string.encode())

hashDb = db["documento"].find_one()

if hashString.hexdigest() == hashDb["hash"]:
    print("São iguais")
else:
    print("Não são iguais")