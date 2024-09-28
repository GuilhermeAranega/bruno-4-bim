from cryptography.fernet import Fernet

chave = Fernet.generate_key()
fernet = Fernet(chave)

arquivo = open("mensagem.txt", "rb")
mensagem = arquivo.read()
arquivo.close()

mensagemCriptografada = fernet.encrypt(mensagem)

arquivo = open("mensagem.txt", "wb")
arquivo.write(mensagemCriptografada)
arquivo.close()

mensagemDescriptografada = fernet.decrypt(mensagemCriptografada)
arquivo = open("mensagemDescriptografada.txt", "wb")
arquivo.write(mensagemDescriptografada)
arquivo.close()

print("Mensagem criptografada e descriptografada com sucesso!")