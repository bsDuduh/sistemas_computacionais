''' "pip install cryptography"
    usar este comando no terminal para 
    fazer o download da biblioteca
'''


from cryptography.fernet import Fernet

# Função para gerar uma chave secreta
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_arquivo:
        chave_arquivo.write(chave)
    print("Chave gerada e salva em 'chave.key'")

# Função para carregar a chave secreta
def carregar_chave():
    with open("chave.key", "rb") as chave_arquivo:
        chave = chave_arquivo.read()
    return chave

# Função para criptografar uma mensagem
def criptografar(mensagem):
    chave = carregar_chave()
    fernet = Fernet(chave)
    mensagem_criptografada = fernet.encrypt(mensagem.encode())
    return mensagem_criptografada

# Função para descriptografar uma mensagem
def descriptografar(mensagem_criptografada):
    chave = carregar_chave()
    fernet = Fernet(chave)
    mensagem_descriptografada = fernet.decrypt(mensagem_criptografada).decode()
    return mensagem_descriptografada

# Exemplo de uso
if __name__ == "__main__":

    gerar_chave()

    mensagem = input("Digite a msg: ")
    
    mensagem_criptografada = criptografar(mensagem)
    print("Mensagem criptografada:", mensagem_criptografada)

    mensagem_descriptografada = descriptografar(mensagem_criptografada)
    print("Mensagem descriptografada:", mensagem_descriptografada)
