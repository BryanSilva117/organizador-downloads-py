import os
import shutil
import time


origem_dir = "C:/Users/a913498/Downloads"


intervalo = 30

while True:
   
    arquivos = os.listdir(origem_dir)

    

    for arquivo in arquivos:

        extensoes = [os.path.splitext(arquivo)[1]]


        for extensao in extensoes:

            nome_extensao = extensao[1:] or "sem-extensoes"

            exits_pasta = os.path.exists(f"C:/Users/a913498/OneDrive - ATOS/Note/Documentos/py-arq-mov/arquivos-{nome_extensao}")

            if exits_pasta == False:
                try:
                    os.mkdir(f"C:/Users/a913498/OneDrive - ATOS/Note/Documentos/py-arq-mov/arquivos-{nome_extensao}")
                    
                except Exception as e:
                    print(f"Erro ao criar a pasta: {e}")
            else:
                print("ja tem pasta")


            destino_dir = f"C:/Users/a913498/OneDrive - ATOS/Note/Documentos/py-arq-mov/arquivos-{nome_extensao}"
                

            if arquivo.endswith(extensao):

                caminho_origem = os.path.join(origem_dir, arquivo)
                caminho_destino = os.path.join(destino_dir, arquivo)
                
                try:
                    
                    shutil.move(caminho_origem, caminho_destino)
                    print(f"Arquivo {arquivo} movido para {destino_dir}")
                except Exception as e:
                    print(f"Erro ao mover o arquivo {arquivo}: {e}")

    print("Nenhum arquivo encontrado!")
    
    time.sleep(intervalo)

