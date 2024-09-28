import hashlib

senha = input("digite a senha: ")

senhaHash = hashlib.sha256(senha.encode())
print(f"hash da senha: {senhaHash.hexdigest()}")