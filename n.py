from cryptography.fernet import Fernet
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/banco")
db = client["banco"]

chave = db["chaves"].find_one()

fernet = Fernet(chave["chave"].encode())

criptografia = input("Digite a mensagem criptografada: ")

msgDescriptografada = fernet.decrypt(criptografia.encode())

print(f"Mensagem descriptografada: {msgDescriptografada.decode()}")