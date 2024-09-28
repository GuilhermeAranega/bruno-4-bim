from cryptography.fernet import Fernet
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/banco")
db = client["banco"]

chave = Fernet.generate_key()
fernet = Fernet(chave)

msg = input("Digite a mensagem: ")

msgCriptografada = fernet.encrypt(msg.encode())

db["criptografia"].insert_one({"chave": chave.decode(), "msg": msgCriptografada.decode()})
print("Mensagem salva no banco de dados")