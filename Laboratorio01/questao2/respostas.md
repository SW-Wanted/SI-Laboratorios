# Questão 2 – Análise de segurança

**a) Qual é a principal diferença entre AES-128 e AES-256?**

R: A principal diferença é o tamanho da chave: 128 bits no AES-128 e 256 bits no AES-256. O AES-256 executa 14 rondas, contra 10 do AES-128, por isso oferece maior margem de segurança e é ligeiramente mais lento. Ambos usam blocos de 128 bits.

**b) Por que motivo não se deve utilizar a mesma chave e o mesmo Nonce repetidamente no AES-GCM?**

R: O GCM cifra em modo contador, logo a mesma chave com o mesmo nonce produz a mesma sequência cifrante. Com dois textos cifrados, um atacante obtém o XOR dos dois textos originais (C1 ⊕ C2 = P1 ⊕ P2) e pode recuperar informação sobre eles. A repetição também pode expor a chave interna de autenticação, o que permite forjar tags válidas.

**c) O que acontece quando um utilizador tenta alterar o conteúdo de um ficheiro cifrado com AES-GCM antes da sua decifragem?**

R: O GCM não impede a alteração do ficheiro, mas detecta-a. Na decifragem, a tag calculada deixa de coincidir com a tag guardada, a operação falha e nenhum texto é devolvido. Na biblioteca `cryptography`, esta falha gera a excepção `InvalidTag`. Sem a chave, o atacante não consegue calcular uma tag válida para o conteúdo alterado.
