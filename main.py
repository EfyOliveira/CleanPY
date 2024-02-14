import os
from colorama import Fore, Style  # Importa cores para terminal

# Define as cores para impressão
COR_IMPORTANTE = Fore.GREEN
COR_REMOVIDO = Fore.RED
COR_PADRAO = Style.RESET_ALL

def limpeza_android(diretorio):
    arquivos_importantes = ['Documentos', 'Videos', 'DCIM']  # Exemplo de arquivos importantes
    arquivos_para_manter = []  # Lista para armazenar os arquivos que não devem ser excluídos

    # Percorre o diretório
    for root, dirs, files in os.walk(diretorio):
        for dir in dirs:
            caminho_completo = os.path.join(root, dir)
            # Verifica se a pasta está vazia
            if not os.listdir(caminho_completo):
                print(f"Pasta vazia encontrada: {caminho_completo}")
                os.rmdir(caminho_completo)
                print(f"{COR_REMOVIDO}Pasta vazia removida: {caminho_completo}{COR_PADRAO}")

        for file in files:
            caminho_completo = os.path.join(root, file)
            # Verifica se o arquivo não está na lista de arquivos importantes
            if file not in arquivos_importantes:
                # Adiciona à lista de arquivos para manter
                arquivos_para_manter.append(caminho_completo)
            else:
                print(f"{COR_IMPORTANTE}Arquivo importante encontrado: {caminho_completo}{COR_PADRAO}")

    # Remove os arquivos que não estão na lista de arquivos para manter
    for arquivo in arquivos_para_manter:
        os.remove(arquivo)
        print(f"{COR_REMOVIDO}Arquivo removido: {arquivo}{COR_PADRAO}")

# Diretório a ser limpo (exemplo)
diretorio_android = "/storage/emulated/0"
limpeza_android(diretorio_android)
