# Questão 6 – Comparação técnica

| Aspecto | Criptografia simétrica | Criptografia assimétrica |
|---|---|---|
| **Gestão de chaves** | Usa uma chave secreta partilhada. Com *n* utilizadores, são precisas n(n−1)/2 chaves para cada par ter a sua. | Cada utilizador tem um par de chaves, pública e privada. Com *n* utilizadores, são precisos *n* pares. |
| **Velocidade de processamento** | Muito rápida, adequada a grandes volumes de dados. | Muito mais lenta, adequada a pequenas quantidades de dados, como chaves de sessão e resumos. |
| **Distribuição de chaves** | Difícil: a chave tem de ser entregue por um canal seguro. | Simples: a chave pública pode ser divulgada, mas a sua autenticidade deve ser garantida, por exemplo, com certificados. |
| **Confidencialidade** | Garantida pela chave secreta. É o método usado para cifrar os dados. | Cifra-se com a chave pública do destinatário e só a sua chave privada decifra. Usada sobretudo para proteger chaves de sessão. |
| **Autenticação e assinatura digital** | Autentica a mensagem com AES-GCM ou HMAC, mas não identifica qual das partes a criou, logo não oferece não repúdio nem assinatura digital. | Suporta assinatura digital com a chave privada, verificável com a chave pública, o que oferece autenticação e não repúdio. |
| **Exemplos de algoritmos** | AES, ChaCha20. | RSA, ECC (ECDSA, ECDH), Ed25519. |
