# Questão 1 – Implementação do AES

A implementação está em `aes_gcm.py`. O script gera a chave, cria o `documento.txt`, cifra-o para `documento.txt.enc`, decifra-o para `documento_decifrado.txt` e compara o resultado com o original.

O ficheiro cifrado guarda, por esta ordem, o nonce (12 bytes), o texto cifrado e a tag (16 bytes). O nonce e a tag podem ser guardados com o texto cifrado porque não são secretos.

**e) Explique a importância do IV/Nonce e da etiqueta de autenticação (Authentication Tag) no AES-GCM.**

R: O nonce garante que a mesma chave produz uma sequência cifrante diferente em cada cifragem. Assim, o mesmo texto cifrado duas vezes gera resultados diferentes. Por isso, nunca deve repetir-se com a mesma chave.

A tag é calculada sobre o texto cifrado e permite verificar a sua integridade e autenticidade. Se o ficheiro for alterado, a verificação falha e a decifragem é recusada.
