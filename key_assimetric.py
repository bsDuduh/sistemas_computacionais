from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives import serialization

# Gerar chave privada e pública
def gerar_chaves():
    chave_privada = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    chave_publica = chave_privada.public_key()
    return chave_privada, chave_publica

# Criptografar mensagem
def criptografar(mensagem, chave_publica):
    mensagem_criptografada = chave_publica.encrypt(
        mensagem.encode(),
        OAEP(
            mgf=MGF1(algorithm=SHA256()),
            algorithm=SHA256(),
            label=None
        )
    )
    return mensagem_criptografada

# Descriptografar mensagem
def descriptografar(mensagem_criptografada, chave_privada):
    mensagem_original = chave_privada.decrypt(
        mensagem_criptografada,
        OAEP(
            mgf=MGF1(algorithm=SHA256()),
            algorithm=SHA256(),
            label=None
        )
    )
    return mensagem_original.decode()

# Testar o código
if __name__ == "__main__":
    chave_privada, chave_publica = gerar_chaves()
    mensagem = "Esta é uma mensagem secreta"
    print(f"Mensagem Original: {mensagem}\n")

    # Criptografar a mensagem
    mensagem_criptografada = criptografar(mensagem, chave_publica)
    print(f"Mensagem Criptografada: {mensagem_criptografada}\n")

    # Descriptografar a mensagem
    mensagem_descriptografada = descriptografar(mensagem_criptografada, chave_privada)
    print(f"Mensagem Descriptografada: {mensagem_descriptografada}")