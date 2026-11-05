# Questão 3 – Implementação do RSA

A implementação está em `rsa_oaep.py`. O script gera o par de chaves RSA de 2048 bits e guarda-as em `chave_privada.pem` e `chave_publica.pem`. A seguir, cifra a mensagem com a chave pública usando RSA-OAEP com SHA-256 e decifra-a com a chave privada. A chave privada fica protegida por senha e não é enviada para o repositório.

**e) Demonstre que apenas a chave privada correspondente consegue recuperar a mensagem cifrada neste cenário.**

R: O script tenta decifrar a mesma mensagem com duas chaves. A chave privada correspondente recupera o texto original. Uma segunda chave privada, gerada para o teste, é recusada com um erro de decifragem, porque o OAEP detecta que o resultado não é válido.

O teste ilustra o comportamento, mas não constitui uma prova. A garantia vem da dificuldade de obter a chave privada a partir da chave pública, que no RSA assenta na factorização de números muito grandes.
