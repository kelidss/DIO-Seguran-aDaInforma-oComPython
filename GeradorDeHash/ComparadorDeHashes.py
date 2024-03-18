import os
import hashlib

# Obtém o diretório do script atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Constrói os caminhos completos para os arquivos h1.txt e h2.txt
arquivo1 = os.path.join(diretorio_atual, "h1.txt")
arquivo2 = os.path.join(diretorio_atual, "h2.txt")

print("Caminho do arquivo 1:", arquivo1)
print("Caminho do arquivo 2:", arquivo2)

hash1 = hashlib.new("ripemd160")
hash1.update(open(arquivo1, "rb").read())

hash2 = hashlib.new("ripemd160")
hash2.update(open(arquivo2, "rb").read())

if hash1.digest() != hash2.digest():
    print(f"O arquivo {arquivo1} é diferente do arquivo {arquivo2}")
    print("Hash arquivo 1: ", hash1.hexdigest())
    print("Hash arquivo 2: ", hash2.hexdigest())
else:
    print(f"O arquivo {arquivo1} é igual ao arquivo {arquivo2}")
    print("Hash arquivo 1: ", hash1.hexdigest())
    print("\nHash arquivo 2: ", hash2.hexdigest())
