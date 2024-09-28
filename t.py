import hashlib

arquivo = open('arquivo.txt', 'r+')

arquivoLido = arquivo.read().encode()
hashArquivo = hashlib.sha256(arquivoLido)

arquivo.write("novo conteudo")
arquivoLidoAlterado = arquivo.read().encode()
hashArquivoAlterado = hashlib.sha256(arquivoLidoAlterado)

print(f"hash do arquivo lido: {hashArquivo.hexdigest()}")
print(f"hash do arquivo alterado: {hashArquivoAlterado.hexdigest()}")

if hashArquivo.hexdigest() == hashArquivoAlterado.hexdigest():
    print("Arquivo não foi alterado")
else:
    print("Arquivo foi alterado")

arquivo.close()