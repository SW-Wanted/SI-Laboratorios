from getpass import getpass
from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa

PASTA = Path(__file__).parent
CHAVE_PRIVADA = PASTA / "assinatura_privada.pem"
CHAVE_PUBLICA = PASTA / "assinatura_publica.pem"
DOCUMENTO = PASTA / "documento.txt"
DOCUMENTO_ALTERADO = PASTA / "documento_alterado.txt"
ASSINATURA = PASTA / "documento.sig"

CONTEUDO = "Autorizo o pagamento de 100 000 Kz ao fornecedor fictício.\n"
CONTEUDO_ALTERADO = "Autorizo o pagamento de 900 000 Kz ao fornecedor fictício.\n"
PSS = padding.PSS(
    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    salt_length=padding.PSS.DIGEST_LENGTH,
)


def gerar_e_guardar_chaves(senha: bytes) -> rsa.RSAPrivateKey:
    privada = rsa.generate_private_key(public_exponent=65537, key_size=2048)
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
    return privada


def assinar(privada: rsa.RSAPrivateKey, dados: bytes) -> bytes:
    return privada.sign(dados, PSS, hashes.SHA256())


def assinatura_valida(dados: bytes, assinatura: bytes) -> bool:
    publica = serialization.load_pem_public_key(CHAVE_PUBLICA.read_bytes())
    try:
        publica.verify(assinatura, dados, PSS, hashes.SHA256())
    except InvalidSignature:
        return False
    return True


def main() -> None:
    senha = getpass("Senha para proteger a chave privada: ").encode("utf-8")
    privada = gerar_e_guardar_chaves(senha)
    print(f"Chaves guardadas: {CHAVE_PRIVADA.name}, {CHAVE_PUBLICA.name}")

    DOCUMENTO.write_text(CONTEUDO, encoding="utf-8")
    ASSINATURA.write_bytes(assinar(privada, DOCUMENTO.read_bytes()))
    assinatura = ASSINATURA.read_bytes()
    print(f"Documento assinado: {ASSINATURA.name} ({len(assinatura)} bytes)")

    valida = assinatura_valida(DOCUMENTO.read_bytes(), assinatura)
    print(f"Assinatura do documento original válida: {valida}")

    DOCUMENTO_ALTERADO.write_text(CONTEUDO_ALTERADO, encoding="utf-8")
    valida = assinatura_valida(DOCUMENTO_ALTERADO.read_bytes(), assinatura)
    print(f"Assinatura do documento alterado válida: {valida}")


if __name__ == "__main__":
    main()
