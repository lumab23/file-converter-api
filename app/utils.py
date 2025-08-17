import os, uuid

BASE_DIR = "uploads"
os.makedirs(BASE_DIR, exist_ok=True)

def gerar_nome_temporario(original_filename: str = "") -> str:
    ext = os.path.splitext(original_filename)[1]  # pega extensão (.rar, .zip, etc)
    return os.path.join(BASE_DIR, f"{uuid.uuid4().hex}{ext}")


def verificar_arq_existe(caminho: str) -> bool: 
    return os.path.isfile(caminho)

def salvar_arquivo_em_disco(filename: str, conteudo: bytes):
    with open(filename, "wb") as f:
        f.write(conteudo)

def ler_arquivo_em_bytes(filename: str) -> bytes:
    with open(filename, "rb") as f:
        return f.read()