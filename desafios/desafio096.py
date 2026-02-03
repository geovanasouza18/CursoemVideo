def area(largura, comprimento):
    area_terreno = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area_terreno}m².')


largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
area(largura, comprimento)