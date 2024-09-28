import pymongo
import hashlib
 
client = pymongo.MongoClient("mongodb://localhost:27017/banco")
db = client["banco"]

senha = input("senha: ")
hashSenha = hashlib.sha256(senha.encode())

db["documento"].insert_one({
    "hash": hashSenha.hexdigest()
})

hashSenhaDb = db["documento"].find_one()["hash"]

senhaDepois = input("Digite a senha: ").encode()
hashSenhaDepois = hashlib.sha256(senhaDepois)

if hashSenhaDepois.hexdigest() == hashSenhaDb:
    print("Senha correta")
else:
    print("Senha incorreta")