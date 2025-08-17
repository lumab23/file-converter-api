import zipfile, os, tempfile, shutil, subprocess

def converter_rar_to_zip(input_file: str, output_file: str):
    pasta_temp = tempfile.mkdtemp()
    try:
        if shutil.which("unrar"):
            comando = ["unrar", "x", "-idq", input_file, pasta_temp]
        elif shutil.which("unar"):
            comando = ["unar", "-quiet", "-o", pasta_temp, input_file]
        else:
            raise Exception("Nenhum extrator RAR encontrado (instale 'unrar' ou 'unar').")

        subprocess.run(comando, check=True)

        # cria zip
        with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, _, files in os.walk(pasta_temp):
                for file in files:
                    file_path = os.path.join(root, file)
                    nome_do_arquivo = os.path.relpath(file_path, pasta_temp)
                    zf.write(file_path, nome_do_arquivo)
    finally:
        shutil.rmtree(pasta_temp)
