from cryptography.fernet import Fernet

chave = Fernet.generate_key()

arquivoChave = open("chave.key", "wb")

arquivoChave.write(chave)

arquivoChave.close()