import os
opcao = 0
qtdTotMerc = [0,0,0,0,0,0,0,0,0,0,0,0]
qtdTotFar  = [0,0,0,0,0,0,0,0,0,0,0,0]
qtdTotConv = [0,0,0,0,0,0,0,0,0,0,0,0]
TotVendBr  = [0,0,0,0,0,0,0,0,0,0,0,0]

meses = ['Jan', 'Fev','Mar','Abr','Mai','Jun','Jul','Ago','Set','Out','Nov','Dez']

while opcao == 0:
    os.system('cls')
    print('* * * Qual sistema deseja acessar? * * * ')
    print('1 - Fábrica')
    print('2 - Distribuidora')
    print('3 - Mercado')
    print('4 - Farmácia')
    print('5 - Loja de Conveniência')
    print('6 - Relatório')
    print('7 - Encerrar')
    opcao = int(input('Digite a opção desejada: '))

    if(opcao == 1): #Fábrica
      os.system('cls') 
      while opcao == 1:
        print('\t* * * Sistema * * * \n')
        print('\t OP - Fábrica \n')
        qtdFabricada = int(input('\tDigite o total de pastas fabricadas: '))
        print(f'\n\tO total de pastas fabricadas é {qtdFabricada} unidades.\n\n')
        opcao = int(input('Digite 0 para retorar ao Menu Principal: '))
    
    if(opcao == 2): #Distribuidora
      os.system('cls') 
      while opcao == 2:
        print('\t* * * Sistema * * * \n')
        print('\t OP - Distribuidora \n')
        print(f'\t Existem {qtdFabricada} unidades disponiveis para distribuir\n')

        unidadesParaMercado = int (input("\tInforme a quantidade para distribuir para Mercados: "))
        restam = qtdFabricada - unidadesParaMercado
        print(f'\tRestam {restam} unidades disponiveis para distribuir\n')

        unidadesParaFarmacia = int (input("\tInforme a quantidade para distribuir para Farmacias: "))
        restam = restam - unidadesParaFarmacia
        print(f'\tRestam {restam} unidades disponiveis para distribuir\n')

        unidadesParaConveniencia = int (input("\tInforme a quantidade para distribuir para Lojas de Conveniência: "))
        restam = restam - unidadesParaConveniencia        
        print(f'\tRestam {restam} unidades disponiveis para distribuir\n')
        
        opcao = int(input('Digite 0 para retorar ao Menu Principal: '))

    if(opcao == 3):   #Mercado
      os.system('cls') 
      while opcao == 3:
        print('\t* * * Sistema * * * \n')
        print('\t OP - Mercado \n')
        print(f'\t Existem {unidadesParaMercado} disponiveis para venda\n')

        while  unidadesParaMercado > 0:
          mesVenda = int(input("Informe o número do mês da venda (1 - 12): "))
          qtdVendMerc = int(input(f"Informe quantas pastas que foram vendidas no mes {mesVenda}: "))
          qtdTotMerc[mesVenda - 1]  = qtdVendMerc          
          unidadesParaMercado = unidadesParaMercado - qtdVendMerc
          print(f'Estoque do mercado: {unidadesParaMercado} unidades\n')

        if(unidadesParaMercado == 0):
          opcao = 0

    if(opcao == 4):   #Farmacia
      os.system('cls') 
      while opcao == 4:
        print('\t* * * Sistema * * * \n')
        print('\t OP - Farmacia \n')
        print(f'\t Existem {unidadesParaFarmacia} disponiveis para venda\n')

        while  unidadesParaFarmacia > 0:
          mesVenda = int(input("Informe o número do mês da venda (1 - 12): "))
          qtdVendFar = int(input(f"Informe quantas pastas que foram vendidas no mes {mesVenda}: "))
          qtdTotFar[mesVenda - 1] = qtdVendFar              
          unidadesParaFarmacia = unidadesParaFarmacia - qtdVendFar
          print(f'Estoque da Farmacia: {unidadesParaFarmacia} unidades\n')
        if(unidadesParaFarmacia == 0):
          opcao = 0

    if(opcao == 5):   #Lojas de Conveniência
      os.system('cls') 
      while opcao == 5:
        print('\t* * * Sistema * * * \n')
        print('\t OP - Lojas de Conveniência \n')
        print(f'\t Existem {unidadesParaConveniencia} disponiveis para venda\n')

        while  unidadesParaConveniencia > 0:
          mesVenda = int(input("Informe o número do mês da venda (1 - 12): "))
          qtdVendConv = int(input(f"Informe quantas pastas que foram vendidas no mes {mesVenda}: "))
          qtdTotConv[mesVenda - 1] = qtdVendConv              
          unidadesParaConveniencia = unidadesParaConveniencia - qtdVendConv
          print(f'Estoque da Loja de Conveniência: {unidadesParaConveniencia} unidades\n')
        if (unidadesParaConveniencia == 0):
          opcao = 0

    if(opcao == 6):   #relatorio
      os.system('cls') 
      while opcao == 6:
        print('\t* * * Sistema * * * \n')
        print('\t OP - Relatório \n')
        print(f'\t Foram vendidos as seguintes quantidades em cada mês\n')
        
        for i in range(len(meses)):
          TotVendBr[i] = qtdTotMerc[i] + qtdTotFar[i] + qtdTotConv[i] 
       
        print('Meses do ano:\t\t\t\t {}'.format(meses))
        print('Vendas em Mercados:\t\t\t {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}'
                   .format(qtdTotMerc[0],qtdTotMerc[1],qtdTotMerc[2],qtdTotMerc[3],qtdTotMerc[4],qtdTotMerc[5],
                           qtdTotMerc[6],qtdTotMerc[7],qtdTotMerc[8],qtdTotMerc[9],qtdTotMerc[10],qtdTotMerc[11]))
                           
        print('Vendas em Farmacias:\t\t\t {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}'
                   .format(qtdTotFar[0],qtdTotFar[1],qtdTotFar[2],qtdTotFar[3],qtdTotFar[4],qtdTotFar[5],
                           qtdTotFar[6],qtdTotFar[7],qtdTotFar[8],qtdTotFar[9],qtdTotFar[10],qtdTotFar[11]))
                           
        print('Vendas em Lojas de Conveniênci:\t\t {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}'
                   .format(qtdTotConv[0],qtdTotConv[1],qtdTotConv[2],qtdTotConv[3],qtdTotConv[4],qtdTotConv[5],
                           qtdTotConv[6],qtdTotConv[7],qtdTotConv[8],qtdTotConv[9],qtdTotConv[10],qtdTotConv[11]))

        print('Totais vendidos no Brasi:\t\t {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}  {:5d}'
                   .format(TotVendBr[0],TotVendBr[1],TotVendBr[2],TotVendBr[3],TotVendBr[4],TotVendBr[5],
                           TotVendBr[6],TotVendBr[7],TotVendBr[8],TotVendBr[9],TotVendBr[10],TotVendBr[11]))
        opcao = int(input('Digite 0 para retorar ao Menu Principal: '))    