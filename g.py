from cryptography.fernet import Fernet

chave = Fernet.generate_key()
fernet = Fernet(chave)

msg = input("Digite uma mensagem: ")

msgCriptografada = fernet.encrypt(msg.encode())
print(f"Mensagem criptografada: {msgCriptografada}")