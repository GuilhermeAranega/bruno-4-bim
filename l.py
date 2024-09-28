from cryptography.fernet import Fernet

chaveArquivo = open("chave.key", "rb")

chave = chaveArquivo.read()

fernet = Fernet(chave)

msg = input("Digite uma mensagem: ")

msgCriptografada = fernet.encrypt(msg.encode())
print(f"Mensagem criptografada: {msgCriptografada}")