import hashlib

string = input("digite a string: ")

stringHash = hashlib.sha256(string.encode())
print(f"hash da string: {hex(int(stringHash.hexdigest(), 16))}")