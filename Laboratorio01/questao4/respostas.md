# Questão 4 – Assinatura digital

A implementação está em `assinatura_pss.py`. O script assina o `documento.txt` com RSA-PSS e SHA-256, guarda a assinatura em `documento.sig` e verifica-a com a chave pública. Usa um par de chaves próprio, separado do par de cifragem da Questão 3, porque uma chave não deve ser usada para fins diferentes.

**c) Altere o conteúdo do documento e volte a verificar a assinatura. Apresente e explique o resultado obtido.**

R: O documento original foi aceite e o documento alterado, em que 100 000 Kz passou a 900 000 Kz, foi rejeitado:

```text
Assinatura do documento original válida: True
Assinatura do documento alterado válida: False
```

A assinatura foi criada sobre o resumo SHA-256 do documento original. Mudar um único carácter gera um resumo completamente diferente, que já não corresponde à assinatura. Por isso, a verificação falha com `InvalidSignature`. Isto prova que o documento foi alterado depois de assinado, e só quem tem a chave privada poderia produzir uma assinatura válida para o novo conteúdo.
