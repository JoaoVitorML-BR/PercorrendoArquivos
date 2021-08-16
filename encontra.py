import os
from convertam import formata_tamanho

caminho_procura = input('Caminho?: ')
termo_procura = input('Termo: ')

conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura): # percorrendo arquivos, porém ele retorna como lista
    for arquivo in arquivos: #resolvendo a questão da lista fazendo esse for, e ai fica um abaixo do outro.
        if termo_procura in arquivo: #verificando se o termo da var termo_procura foi achado, se for ele executa.
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo) #aqui estou juntado o nome da raiz + arquivo (pasta e o nome do arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo) # nome do arquivo + extensão
                tamanho = os.path.getsize(caminho_completo) # aqui ele está verificando o tamanho do arquivo.

                print()
                print('Encontrei o arquivo:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensão:', ext_arquivo)
                print('Tamanho', tamanho)
                print('Tamanho formatado:', formata_tamanho(tamanho))
            except PermissionError as e:
                print('Sem Permissões')
            except FileNotFoundError as e:
                print('Arquivo não encontrado')
            except Exception as e:
                print('Erro desconhecido', e)

print()
print(f'{conta} arquivo(s) encontrado(s).')