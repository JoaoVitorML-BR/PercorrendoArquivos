'''
aqui foi feita uma função que verifica o tamanho do arquivo, ou seja, foi feio uma formula para calcular o valor
e se o valor retornado pela var lá dentro de encontra.py na var tamanho for menor que kilo por exemplo ele seta com um B
indicando ser Byte (para colocar no print), se for menor que mega ele seta com um k, indicandos er kilobyte
'''

def formata_tamanho(tamanho):

    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        tamanho = base
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'
    tamanho = round(tamanho, 2) #formatando as casas o 2 indica que são 2 casas decimais.
    return f'{tamanho}{texto}'.replace('.', ',') # retornando na var tamanho o tamanho + a letra