# Questão 5 – Estudo de caso

**a) Indique qual dos algoritmos, AES ou RSA, seria mais adequado para cifrar grandes quantidades de dados. Justifique.**

R: O AES, por ser muito mais rápido e cifrar dados de qualquer tamanho prático, sobretudo com aceleração por hardware. O RSA é lento e só cifra blocos pequenos: com chave de 2048 bits, OAEP e SHA-256, o limite é de 190 bytes por operação.

**b) Explique como a combinação de criptografia simétrica e assimétrica pode ser utilizada para proteger a comunicação.**

R: Usa-se criptografia híbrida:

1. O funcionário gera uma chave de sessão AES-256 aleatória.
2. Cifra a mensagem com essa chave em AES-GCM, o que garante confidencialidade e integridade.
3. Cifra a chave de sessão com a chave pública RSA do servidor, usando OAEP.
4. Assina a mensagem com a sua chave privada, usando RSA-PSS.
5. O servidor decifra a chave de sessão com a sua chave privada, decifra a mensagem e verifica a assinatura com a chave pública do funcionário.

Assim, o AES trata do volume de dados e o RSA resolve a distribuição da chave e a autenticação. As chaves públicas devem ser validadas por certificados digitais, para evitar que um atacante substitua uma chave pela sua.

**c) Explique a importância da assinatura digital neste cenário.**

R: A assinatura prova quem enviou a mensagem e que ela não foi alterada, porque só o titular tem a chave privada. A tag do GCM não basta para isso, pois qualquer pessoa com a chave de sessão consegue gerá-la. A assinatura também suporta o não repúdio, importante numa instituição financeira, já que o remetente dificilmente pode negar uma operação que assinou.
