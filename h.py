from cryptography.fernet import Fernet

chave = Fernet.generate_key()
fernet = Fernet(chave)

msg = input("Digite a mensagem: ")

msgCriptografada = fernet.encrypt(msg.encode())
print(f"Mensagem criptografada: {msgCriptografada}")

criptografia = input("Digite a criptografia: ")

msgDescriptografada = fernet.decrypt(criptografia.encode())

print(f"Mensagem descriptografada: {msgDescriptografada}")