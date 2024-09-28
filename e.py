import hashlib

senha = input("digite a senha: ")

senhaHash = hashlib.md5(senha.encode())
print(f"hash da senha: {senhaHash.hexdigest()}")