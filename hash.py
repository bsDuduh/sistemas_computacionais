import hashlib

# Função para gerar um hash
def gerar_hash(mensagem, algoritmo="sha256"):
    try:
        # Selecionar o algoritmo de hash
        if algoritmo == "md5":
            hash_obj = hashlib.md5()
        elif algoritmo == "sha256":
            hash_obj = hashlib.sha256()
        elif algoritmo == "sha512":
            hash_obj = hashlib.sha512()
        else:
            raise ValueError("Algoritmo não suportado!")
        
        # Atualizar o hash com a mensagem
        hash_obj.update(mensagem.encode())
        
        # Retornar o hash hexadecimal
        return hash_obj.hexdigest()
    except Exception as e:
        return str(e)

# Testando a função
if __name__ == "__main__":
    mensagem = "Mensagem secreta"
    algoritmo = "sha256"
    resultado_hash = gerar_hash(mensagem, algoritmo)
    print(f"Mensagem: {mensagem}")
    print(f"Hash ({algoritmo}): {resultado_hash}")