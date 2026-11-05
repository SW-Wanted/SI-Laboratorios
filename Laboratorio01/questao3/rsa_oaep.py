from getpass import getpass
from pathlib import Path

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

PASTA = Path(__file__).parent
CHAVE_PRIVADA = PASTA / "chave_privada.pem"
CHAVE_PUBLICA = PASTA / "chave_publica.pem"
MENSAGEM_CIFRADA = PASTA / "mensagem_cifrada.bin"

MENSAGEM = "Mensagem de teste entre os departamentos.".encode("utf-8")
OAEP = padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None,
)


def gerar_par() -> rsa.RSAPrivateKey:
    return rsa.generate_private_key(public_exponent=65537, key_size=2048)


def guardar_chaves(privada: rsa.RSAPrivateKey, senha: bytes) -> None:
    CHAVE_PRIVADA.write_bytes(
        privada.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(senha),
        )
    )
    CHAVE_PRIVADA.chmod(0o600)
    CHAVE_PUBLICA.write_bytes(
        privada.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
    )


def cifrar(mensagem: bytes) -> bytes:
    publica = serialization.load_pem_public_key(CHAVE_PUBLICA.read_bytes())
    return publica.encrypt(mensagem, OAEP)


def decifrar(cifrada: bytes, senha: bytes) -> bytes:
    privada = serialization.load_pem_private_key(
        CHAVE_PRIVADA.read_bytes(), password=senha
    )
    return privada.decrypt(cifrada, OAEP)


def tentar_decifrar_com_outra_chave(cifrada: bytes) -> None:
    outra_privada = gerar_par()
    try:
        outra_privada.decrypt(cifrada, OAEP)
    except ValueError:
        print("Outra chave privada: decifragem recusada")
    else:
        print("Outra chave privada: decifragem aceite")


def main() -> None:
    senha = getpass("Senha para proteger a chave privada: ").encode("utf-8")

    privada = gerar_par()
    print(f"Par de chaves gerado: {privada.key_size} bits")

    guardar_chaves(privada, senha)
    print(f"Chaves guardadas: {CHAVE_PRIVADA.name}, {CHAVE_PUBLICA.name}")

    cifrada = cifrar(MENSAGEM)
    MENSAGEM_CIFRADA.write_bytes(cifrada)
    print(f"Mensagem cifrada: {MENSAGEM_CIFRADA.name} ({len(cifrada)} bytes)")

    recuperada = decifrar(MENSAGEM_CIFRADA.read_bytes(), senha)
    print(f"Chave privada correspondente: {recuperada.decode('utf-8')}")
    print(f"Igual à original: {recuperada == MENSAGEM}")

    tentar_decifrar_com_outra_chave(cifrada)


if __name__ == "__main__":
    main()
