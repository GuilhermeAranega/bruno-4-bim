import hashlib

string1 = input("primeira string: ")
string2 = input("segunda string: ")

hashUm = hashlib.sha256(string1.encode())
hashDois = hashlib.sha256(string2.encode())

if hashUm.hexdigest() == hashDois.hexdigest():
    print("São strings iguais")
else:
    print("Não são strings iguais")