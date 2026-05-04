producao_leite = []
producao_derivados = []
leite_disponivel = 0

produtos = []
derivados = []

while True:
    op = input('\n ------O que deseja fazer?------ \n 1-Gerenciar leite e derivados \n 2-Gerenciar estoque geral \n 3-Verificar estoque geral \n 0-Retornar ao menu \n')
    if op == '1':
        while True:
            gerenciar_leite = input('\n ---Gerenciamento leite e derivados--- \n 1-Produção de leite \n 2-Produção de derivados \n 3-Historico da produção \n 0-Cancelar')

            if gerenciar_leite == '1':
               dia = input('Digite o dia atual: ')
               litros = float(input('Digite a quantia ordenhada(L): '))

               atualizar_valor = [dia, litros]
               producao_leite.append(atualizar_valor)
               leite_disponivel = leite_disponivel + litros

               print('Produção cadastrada.')
            
            elif gerenciar_leite == '2':
                while True:
                    gerenciar_derivados = input('\n ----Gerenciar derivados---- \n 1-Registrar derivado \n 2-Produzir derivado \n 3-Status de produção \n 0-Cancelar \n ')

                    if gerenciar_derivados == '1':
                        novo_derivado = input('Qual derivado deseja adicionar? \n (1)Queijo \n (2)Iogurte \n (3)Manteiga \n (0)Cancelar \n')

                        if novo_derivado == '1':
                            categoria = 'Queijo'
                            tipo = input('Qual tipo de queijo deseja adicionar? ')
                            derivados.append([categoria, tipo])
                        elif novo_derivado == '2':
                            categoria = 'Iogurte'
                            tipo = input('Qual sabor de iogurt deseja adicionar? ')
                            derivados.append([categoria, tipo])
                        elif novo_derivado == '3':
                            categoria = 'Manteiga'
                            tipo = input('Qual tipo de manteiga deseja adicionar? ')
                            derivados.append([categoria, tipo])
                        else:
                            print('Retornando ao menu.')

                
                    elif gerenciar_derivados == '2':
                    
                        print('\n ----Leite disponível---- \n ', leite_disponivel, 'Litros. \n')
                        print("Derivados registrados:")
                        for i in range(len(derivados)):
                            print(f"({i+1}) {derivados[i][0]} {derivados[i][1]}")
                        print('(0)Cancelar.')                    
                        produzir = int(input('Qual derivado foi produzido? \n'))

                        if produzir == 0:
                            print('Retornando ao menu.')
                        else:
                            indice = produzir - 1
                            derivado_escolhido = derivados[indice]

                            quantidade_produzida = float(input('Qual a quantia produzida?(Kg ou L): '))
                            gasto_leite = float(input('Quantos litros de leite foram gastos?(L): '))
                            leite_disponivel -= gasto_leite
                            producao_derivados.append([derivado_escolhido[0], derivado_escolhido[1], quantidade_produzida])
                            print('Estoque atualizado com sucesso. \n Leite Gasto: ', gasto_leite, 'Litros \n Leite total: ', leite_disponivel, 'Litros')

                    elif gerenciar_derivados == '3':
                        print(f'\nLeite disponível: {leite_disponivel} L\n')

                        if len(producao_derivados) == 0:
                            print("Nenhum derivado produzido ainda.")
                        else:
                            print("Derivados disponíveis:")
                            for item in producao_derivados:
                                if item[0] == 'Iogurte':
                                    unidade = 'L'
                                else:
                                    unidade = 'kg'
                                    print(f"{item[0]} {item[1]}: {item[2]} {unidade}")
                        

                    elif gerenciar_leite == '0':
                        break                            
   
    #elif op == '2':


    
