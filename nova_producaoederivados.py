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
                        if len(derivados) == 0:
                            print('Nenhum derivado cadastrado.')
                            continue
                        for i in range(len(derivados)):
                            print(f"({i+1}) {derivados[i][0]} {derivados[i][1]}")
                        print('(0)Cancelar.')                    
                        produzir = int(input('Qual derivado foi produzido? \n'))
                        if produzir == 0:
                            break
                        elif produzir < 0 or produzir > len(derivados):
                            print('Retornando ao menu.')
                            continue
                        else:
                            indice = produzir - 1
                            derivado_escolhido = derivados[indice]

                            quantidade_produzida = float(input('Qual a quantia produzida?(Kg ou L): '))
                            gasto_leite = float(input('Quantos litros de leite foram gastos?(L): '))
                            if gasto_leite > leite_disponivel:
                                print('Leite insuficiente.')
                                continue
                            else:
                                leite_disponivel -= gasto_leite
                                producao_derivados.append([derivado_escolhido[0], derivado_escolhido[1], quantidade_produzida])
                                print('Estoque atualizado com sucesso.')
                            print(' \n Leite Gasto: ', gasto_leite, 'Litros \n Leite total: ', leite_disponivel, 'Litros')

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
                    
                    elif gerenciar_derivados == '0':
                        break
                    
                    else:
                        print('Opção inválida.')
                        

            elif gerenciar_leite == '0':
                break     
            else:
                print('Validação Invalida')                       
   
    elif op == '2':
        while True:
            gerenciar_estoque = input('\n----Gerenciamento de estoque----\n1-Gerenciar produto do rebanho\n2-Atualizar estoque\n3-Ver Estoque\n0-Cancelar\n')
            
            if gerenciar_estoque == '1':
                registro_produto = input('\n----Qual produto deseja registrar?----\n(1)Carne\n(2)Ovos\n(3)Lã\n(4)Pele\n(5)Banha\n(0)Cancelar\n')
                
                if registro_produto == '0':
                    continue
                elif registro_produto == '1':
                    carne_escolha = input('\n----CARNES----\n(1)Bovina\n(2)Suínos\n(3)Aves\n(4)Caprino\n(5)Ovino\n(0)Cancelar\n')
                    if carne_escolha == '0':
                        continue
                    elif carne_escolha == '1':
                        animal = 'Bovina'
                    elif carne_escolha == '2':
                        animal = 'Suínos'
                    elif carne_escolha == '3':
                        animal = 'Aves'
                    elif carne_escolha == '4':
                        animal = 'Caprino'
                    elif carne_escolha == '5':
                        animal = 'Ovino'
                    else:
                        print('Opção inválida.')
                        continue
                    tipo_produto = 'Carne'
                elif registro_produto == '2':
                    tipo_produto = 'Ovos'
                    animal = ''
                elif registro_produto == '3':
                    tipo_produto = 'Lã'
                    animal = ''
                elif registro_produto == '4':
                    tipo_produto = 'Pele'
                    animal = ''
                elif registro_produto == '5':
                    tipo_produto = 'Banha'
                    animal = ''
                else:
                    print('Opção inválida.')
                    continue

                quantidade = float(input('Digite a quantidade disponível: '))
                
                # Verificar se o produto já existe
                existe = 0
                for p in produtos:
                    if p[0] == tipo_produto and p[1] == animal:
                        p[2] += quantidade
                        print('Produto existente atualizado. Nova quantidade:', p[2])
                        existe = 1
                        break
                if existe == 0:
                    produtos.append([tipo_produto, animal, quantidade])
                    if animal == '':
                        print(str(quantidade) + ' de ' + tipo_produto + ' adicionados ao estoque.')
                    else:
                        print(str(quantidade) + ' de ' + tipo_produto + ' (' + animal + ') adicionados ao estoque.')

            elif gerenciar_estoque == '2':
                # Atualizar estoque
                if len(produtos) == 0:
                    print('Nenhum produto cadastrado para atualizar.')
                    continue

                print('\nProdutos disponíveis:')
                for i in range(len(produtos)):
                    if produtos[i][1] == '':
                        print(f"{i+1} - {produtos[i][0]}: {produtos[i][2]}")
                    else:
                        print(f"{i+1} - {produtos[i][0]} ({produtos[i][1]}): {produtos[i][2]}")

                escolha = int(input('Digite o número do produto que deseja atualizar (0 para cancelar): '))
                if escolha == 0:
                    continue
                if escolha < 1 or escolha > len(produtos):
                    print('Opção inválida.')
                    continue

                indice = escolha - 1
                acao = input('Digite 1 para adicionar quantidade ou 2 para remover quantidade: ')
                if acao == '1':
                    qtd = float(input('Digite a quantidade a adicionar: '))
                    produtos[indice][2] += qtd
                    print('Estoque atualizado. Nova quantidade:', produtos[indice][2])
                elif acao == '2':
                    qtd = float(input('Digite a quantidade a remover: '))
                    if qtd > produtos[indice][2]:
                        print('Erro: quantidade maior que o estoque disponível.')
                    else:
                        produtos[indice][2] -= qtd
                        print('Estoque atualizado. Nova quantidade:', produtos[indice][2])
                else:
                    print('Ação inválida.')

            elif gerenciar_estoque == '3':
                # Ver estoque
                print('\n--- Estoque de Leite ---')
                print(leite_disponivel, 'litros')

                print('\n--- Derivados ---')
                if len(producao_derivados) == 0:
                    print('Nenhum derivado produzido.')
                else:
                    for item in producao_derivados:
                        if item[0] == 'Iogurte':
                            unidade = 'L'
                        else:
                            unidade = 'kg'
                        print(f"{item[0]} {item[1]}: {item[2]} {unidade}")

                print('\n--- Produtos do Rebanho ---')
                if len(produtos) == 0:
                    print('Nenhum produto registrado.')
                else:
                    for p in produtos:
                        if p[1] == '':
                            print(f"{p[0]}: {p[2]}")
                        else:
                            print(f"{p[0]} ({p[1]}): {p[2]}")

            elif gerenciar_estoque == '0':
                break

            else:
                print('Opção inválida.')                   

    elif op == '3':
        print('\n----- ESTOQUE GERAL -----\n')
        
        print('--- Leite ---')
        print(leite_disponivel, 'litros\n')
        
        print('--- Derivados ---')
        if len(producao_derivados) == 0:
            print('Nenhum derivado produzido.\n')
        else:
            for i in range(len(producao_derivados)):
                item = producao_derivados[i]
                if item[0] == 'Iogurte':
                    unidade = 'L'
                else:
                    unidade = 'kg'
                print(f"{item[0]} {item[1]}: {item[2]} {unidade}")
            print()  

        print('--- Produtos do Rebanho ---')
        if len(produtos) == 0:
            print('Nenhum produto registrado.\n')
        else:
            for i in range(len(produtos)):
                if produtos[i][1] == '':
                    print(f"{produtos[i][0]}: {produtos[i][2]}")
                else:
                    print(f"{produtos[i][0]} ({produtos[i][1]}): {produtos[i][2]}")
            print() 
    
    elif op == '0':
        break