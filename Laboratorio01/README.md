# 🗂 Laboratório 01 - Criptografia Simétrica e Assimétrica

## Enunciado
O enunciado desta avaliação encontre-se em [Enunciado](./ENUNCIADO.md).

## Estrutura
| Pasta | Conteúdo |
|---|---|
| `questao1/` | Implementação do AES-256-GCM |
| `questao2/` | Análise de segurança |
| `questao3/` | Implementação do RSA-OAEP |
| `questao4/` | Assinatura digital RSA-PSS |
| `questao5/` | Estudo de caso |
| `questao6/` | Comparação técnica |

## Execução

### 1. Criar e ativar o ambiente virtual

Na pasta `Laboratorio01`:

```powershell
py -3.15 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Instalar as dependências

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 3. Executar as questões

```powershell
python .\questao1\aes_gcm.py
python .\questao3\rsa_oaep.py
python .\questao4\assinatura_pss.py
```

### 4. Desativar o ambiente

```powershell
deactivate
```
