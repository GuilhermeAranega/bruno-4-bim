from cryptography.fernet import Fernet
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/banco")
db = client["banco"]

chave = Fernet.generate_key()
fernet = Fernet(chave)

msg = input("Digite a mensagem (0 para parar): ")
while msg != "0":
    msg = msg.encode()
    msgCriptografada = fernet.encrypt(msg)

    db["mensagens"].insert_one({"mensagem": msgCriptografada})

    msg = input("Digite a mensagem (0 para parar): ")

print("Mensagens criptografadas armazenadas no banco")