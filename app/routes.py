# o fast api ajuda a organizar a api em partes separadas
# pode criar rotas separadas para diferentes funcionalidades
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
from app.utils import gerar_nome_temporario, verificar_arq_existe
import os 
from app.services import converter_rar_to_zip

# instância da classe APIRouter  
router = APIRouter() 

@router.get("/")
def health_check(): # somente para ver se a api está funcionando
    return {"status": "ok"}

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)): 
    # nome temp. seguro
    if not file.filename:
        raise HTTPException(status_code=400, detail="nome do arquivo é obrigatório")
    
    # validar a extensão do aquivo
    original_filename = file.filename
    if not original_filename.lower().endswith(".rar"):
        raise HTTPException(status_code=400, detail="Apenas arquivos .rar são permitidos")

    filename = gerar_nome_temporario(original_filename)


    # salvar arquivo em disco em chunks
    try:
        with open(filename, "wb")as f:
            while chunk := await file.read(1024 * 1024): # lê de 1mb em 1mb
                f.write(chunk)
    except IOError as e:
        # se ocorrer um erro, levanta uma exceção HTTP
        raise HTTPException(status_code=500, detail=f"Erro ao salvar o arquivo: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {e}")

    return {"status": "arquivo recebido com sucesso", "filename": os.path.basename(filename)}

@router.post("/convert")
async def convert_file(filename: str):
    rar_path = os.path.join("uploads", filename)

    if not verificar_arq_existe(rar_path):
        raise HTTPException(status_code=404, detail="Arquivo RAR não encontrado")
    
    # cria o caminho para o arquivo zip de saída 
    zip_filename = os.path.splitext(os.path.basename(rar_path))[0] + ".zip"
    zip_path = gerar_nome_temporario(zip_filename)

    try: 
        converter_rar_to_zip(rar_path, zip_path)
    except Exception as e:
        # remove o arquivo zip incompleto se existir
        if os.path.exists(zip_path):
            os.remove(zip_path)
        raise HTTPException(status_code=500, detail=f"Erro ao converter arquivo: {e}")
    
    os.remove(rar_path)  # remove o arquivo RAR original após a conversão (isso economiza espaço)

    return {"status": "arquivo convertido com sucesso", "filename": os.path.basename(zip_path)}

@router.get("/download/{filename}")
def download_file(filename: str):
    # constroi o arquivo completo do arquivo de forma segura
    full_path = os.path.join("uploads", filename)
    if not verificar_arq_existe(full_path):
        raise HTTPException(status_code=404, detail="Arquivo não encontrado")
    
    return FileResponse(full_path, media_type='application/zip', filename=filename)