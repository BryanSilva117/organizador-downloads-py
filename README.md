# organizador-downloads-py
Repositório destinado para o projeto de organização do pasta downloads



## Introdução
Este projeto tem como intuito organizar automaticamente a pasta de downloads, movendo os arquivos delas para pastas criada com base na extensão dos arquivos

## Config
Instruções de como configurar.

```bash
# Altere a origem_dir para o diretorio que deseja organizar:
origem_dir = "C:/Users/seu-user/Downloads"
# Altere o exits_pasta para o diretorio onde você quer mover os arquivos
exits_pasta = os.path.exists(f"C:/Users/seu-user/Note/Documentos/py-arq-mov/arquivos-{nome_extensao}") # não mude o {nome_extensao}
# Também altere o destino_dir para o mesmo destino que você deseja
destino_dir = f"C:/Users/seu-user/Note/Documentos/py-arq-mov/arquivos-{nome_extensao}" # não mude o {nome_extensao}
# Rode o arquivo MovingArq.py
py MovingArq.py
```
