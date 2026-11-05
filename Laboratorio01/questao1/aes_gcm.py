from os import urandom
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

PASTA = Path(__file__).parent
CHAVE = PASTA / "chave_aes.key"
DOCUMENTO = PASTA / "documento.txt"
CIFRADO = PASTA / "documento.txt.enc"
DECIFRADO = PASTA / "documento_decifrado.txt"

TAMANHO_NONCE = 12
CONTEUDO = (
    "Funcionária: Ana Exemplo\n"
    "Salário: 450 000 Kz\n"
    "Informação confidencial fictícia.\n"
)


def gerar_chave() -> bytes:
    chave = AESGCM.generate_key(bit_length=256)
    CHAVE.write_bytes(chave)
    CHAVE.chmod(0o600)
    return chave


## @brief Cifra dados com AES-256-GCM usando um nonce novo.
#  @return Bytes no formato nonce (12) || texto cifrado || tag (16).
def cifrar(chave: bytes, dados: bytes) -> bytes:
    nonce = urandom(TAMANHO_NONCE)
    return nonce + AESGCM(chave).encrypt(nonce, dados, None)


def decifrar(chave: bytes, pacote: bytes) -> bytes:
    nonce = pacote[:TAMANHO_NONCE]
    cifrado = pacote[TAMANHO_NONCE:]
    return AESGCM(chave).decrypt(nonce, cifrado, None)


def main() -> None:
    chave = gerar_chave()
    print(f"Chave gerada: {len(chave) * 8} bits -> {CHAVE.name}")

    DOCUMENTO.write_text(CONTEUDO, encoding="utf-8")
    original = DOCUMENTO.read_bytes()
    print(f"Documento criado: {DOCUMENTO.name} ({len(original)} bytes)")

    pacote = cifrar(chave, original)
    CIFRADO.write_bytes(pacote)
    print(f"Documento cifrado: {CIFRADO.name} ({len(pacote)} bytes)")
    print(f"Nonce: {pacote[:TAMANHO_NONCE].hex()}")
    print(f"Tag: {pacote[-16:].hex()}")

    recuperado = decifrar(chave, CIFRADO.read_bytes())
    DECIFRADO.write_bytes(recuperado)
    print(f"Documento decifrado: {DECIFRADO.name}")
    print(recuperado.decode("utf-8"), end="")
    print(f"Igual ao original: {recuperado == original}")


if __name__ == "__main__":
    main()
