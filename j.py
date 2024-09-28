from cryptography.fernet import Fernet
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/banco")
db = client["banco"]

data = db["criptografia"].find_one()

chave = data["chave"].encode()
fernet = Fernet(chave)

msgDescriptografada = fernet.decrypt(data["msg"].encode())

print(f"Mensagem descriptografada: {msgDescriptografada.decode()}")