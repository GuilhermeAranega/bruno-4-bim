from cryptography.fernet import Fernet
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/banco")
db = client["banco"]

chave = Fernet.generate_key()

db["chaves"].insert_one({"chave": chave.decode()})
print("Chave salva no banco de dados")