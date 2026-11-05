<div align="center">

**ISPTEC**

**CURSO DE ENGENHARIA INFORMÁTICA**

**DISCIPLINA: SEGURANÇA INFORMÁTICA**

# AVALIAÇÃO PRÁTICA COM CONSULTA

**Tema: Criptografia Simétrica e Assimétrica**

</div>

| | |
|---|---|
| **Duração:** 120 minutos | **Cotação:** 20 valores |
| **Modalidade:** Individual | **Consulta:** Permitida |
| **Ferramentas:** OpenSSL, Python 3 e biblioteca cryptography | |

## 1. OBJECTIVOS DA AVALIAÇÃO

- Compreender e aplicar os princípios da criptografia simétrica e assimétrica.
- Implementar mecanismos de cifragem e decifragem.
- Gerar e gerir chaves criptográficas.
- Utilizar os algoritmos AES e RSA.
- Compreender as diferenças entre confidencialidade, integridade e autenticidade.
- Aplicar mecanismos criptográficos na protecção da informação.

## 2. ENUNCIADO PRÁTICO

### GRUPO I – CRIPTOGRAFIA SIMÉTRICA (7 valores)

#### Questão 1 – Implementação do AES (4 valores)

Uma instituição pretende proteger os documentos confidenciais dos seus funcionários através de criptografia simétrica. Utilizando Python ou OpenSSL, realize as seguintes actividades:

- Gere uma chave criptográfica de 256 bits para utilização com AES. (1 valor)
- Crie um ficheiro de texto denominado **documento.txt**, contendo uma informação confidencial fictícia. (0,5 valores)
- Implemente a cifragem do ficheiro utilizando o algoritmo AES-256-GCM. (1 valor)
- Realize a decifragem do ficheiro e demonstre que a informação original foi recuperada correctamente. (1 valor)
- Explique a importância do IV/Nonce e da etiqueta de autenticação (Authentication Tag) no AES-GCM. (0,5 valores)

#### Questão 2 – Análise de segurança (3 valores)

- Qual é a principal diferença entre AES-128 e AES-256? (1 valor)
- Por que motivo não se deve utilizar a mesma chave e o mesmo Nonce repetidamente no AES-GCM? (1 valor)
- O que acontece quando um utilizador tenta alterar o conteúdo de um ficheiro cifrado com AES-GCM antes da sua decifragem? (1 valor)

### GRUPO II – CRIPTOGRAFIA ASSIMÉTRICA (7 valores)

---

*ISPTEC | Engenharia Informática | Segurança Informática — Página 1*

---

#### Questão 3 – Implementação do RSA (4 valores)

Uma empresa pretende implementar um mecanismo de comunicação segura entre dois departamentos. Utilizando OpenSSL ou Python, realize as seguintes actividades:

- Gere um par de chaves RSA com 2048 bits. (1 valor)
- Exporte e guarde a chave pública e a chave privada em ficheiros separados. (0,5 valores)
- Utilize a chave pública para cifrar uma mensagem de teste, recorrendo ao esquema RSA-OAEP com SHA-256. (1 valor)
- Utilize a chave privada correspondente para decifrar a mensagem. (1 valor)
- Demonstre que apenas a chave privada correspondente consegue recuperar a mensagem cifrada neste cenário. (0,5 valores)

#### Questão 4 – Assinatura digital (3 valores)

- Crie uma assinatura digital de um documento utilizando RSA-PSS com SHA-256. (1 valor)
- Verifique a assinatura digital utilizando a chave pública. (1 valor)
- Altere o conteúdo do documento e volte a verificar a assinatura. Apresente e explique o resultado obtido. (1 valor)

### GRUPO III – ANÁLISE E APLICAÇÃO (6 valores)

#### Questão 5 – Estudo de caso (3 valores)

Uma instituição financeira pretende implementar um sistema de comunicação segura entre os seus funcionários e o servidor central. O sistema deverá garantir confidencialidade das mensagens, integridade dos dados transmitidos, autenticidade do remetente e protecção contra alterações não autorizadas.

- Indique qual dos algoritmos, AES ou RSA, seria mais adequado para cifrar grandes quantidades de dados. Justifique. (1 valor)
- Explique como a combinação de criptografia simétrica e assimétrica pode ser utilizada para proteger a comunicação. (1 valor)
- Explique a importância da assinatura digital neste cenário. (1 valor)

#### Questão 6 – Comparação técnica (3 valores)

Elabore uma tabela comparativa entre criptografia simétrica e assimétrica, considerando os seguintes aspectos: gestão de chaves; velocidade de processamento; distribuição de chaves; confidencialidade; autenticação e assinatura digital; exemplos de algoritmos.

## 3. ENTREGÁVEIS

- Relatório técnico em formato PDF, contendo a descrição dos procedimentos realizados.
- Código-fonte desenvolvido, quando aplicável.
- Ficheiros utilizados nos testes de cifragem e decifragem.
- Evidências dos resultados obtidos (capturas de ecrã).
- Demonstração prática dos mecanismos implementados, quando solicitada pelo docente.

## 4. CRITÉRIOS DE AVALIAÇÃO

---

*ISPTEC | Engenharia Informática | Segurança Informática — Página 2*

---

| Critério | Cotação |
|---|---|
| Implementação da criptografia simétrica | 7 valores |
| Implementação da criptografia assimétrica | 7 valores |
| Análise e aplicação dos conceitos | 4 valores |
| Organização e qualidade das evidências | 2 valores |
| **Total** | **20 valores** |

## 5. ORIENTAÇÕES GERAIS

- A avaliação é individual e permite consulta de materiais didácticos e documentação técnica.
- Não é permitido apresentar códigos de terceiros como sendo de autoria própria.
- Os estudantes devem compreender e explicar os procedimentos implementados.
- Devem ser utilizadas apenas mensagens e documentos fictícios.
- As chaves privadas devem ser protegidas e não devem ser partilhadas.
- Todos os resultados devem ser devidamente documentados.

<div align="center">

**BOM TRABALHO!**

</div>

---

*ISPTEC | Engenharia Informática | Segurança Informática — Página 3*