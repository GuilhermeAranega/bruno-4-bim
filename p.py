import hashlib

mensagem = input("mensagem: ")

hashmd5 = hashlib.md5(mensagem.encode())
hash1 = hashlib.sha1(mensagem.encode())
hash256 = hashlib.sha256(mensagem.encode())

print(f"hash em md5: {hashmd5.hexdigest()}")
print(f"hash em SHA-1: {hash1.hexdigest()}")
print(f"hash em SHA-256: {hash256.hexdigest()}")

print(f"Tamanho md5: {len(hashmd5.hexdigest())}")
print(f"Tamanho SHA-1: {len(hash1.hexdigest())}")
print(f"Tamanho SHA-256: {len(hash256.hexdigest())}")