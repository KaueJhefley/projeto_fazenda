
user_adm = []
password_adm = []
user_c = []
password_c = []
bovinos = []
suinos = []
aves = []
caprino = []
ovino = []
producao_leite = []
producao_derivados = []
leite_disponivel = 0
preco_leite = 0
derivados = []
produtos = []
receitas = []
despesas = []
saldo = 0
op = -99
index = -99
menu = -99
while menu != 0:
    menu = int(input('----MENU---- \n 1-Fazer login \n 2-Registrar \n 0-Fechar o programa \n'))
    if menu == 1:
        ml = int(input('1-Fazer login como ADM \n 2-fazer login como Cliente \n 0-Fechar o programa \n'))
        if ml == 1:
            id = input('Digite o nome de usuario: ')
            senha = input('Digite sua senha: ')
            if id in user_adm:
                i = user_adm.index(id)
                if senha == password_adm[i]:
                    print(f'Bem vindo ADM {id}')
                    menu_adm = input('1-gerenciar rebanho\n 2-gerenciar produçao e derivados\n 3-gerenciamento financeiro \n 4-gerenciar maquinas\n')
                    if menu_adm == '1':
                        op = -99
                        while op != '0':
                            op = input('------O que deseja fazer?------ \n 1-Cadastrar Animal \n 2-Buscar Animal \n 3-Atualizar Rebanho \n 4-Remover \n 5-gerenciamento de lotes \n 0-retornar ao menu \n')
                            if op == '1':
                                tipo = input('----Que tipo de animal deseja registrar---- \n 1-bovino \n 2-suino \n 3-ave \n 4-caprino\n5-ovino')
                                if tipo == '1':
                                    lista = bovinos
                                elif tipo == '2':
                                    lista = suinos
                                elif tipo == '3':
                                    lista = aves
                                elif tipo == '4':
                                    lista = caprino
                                elif tipo == '5':
                                    lista = ovino
                                else:
                                    print('Tipo inválido')
                                    continue

                                identificacao = input('Digite a identificação do animal: ')
                                status = input('Qual o status do animal\n1-saudavel\n2-prenha ou choca\n3-doente\n')
                                if status == '1':
                                    status = 'saudavel'
                                elif status == '2':
                                    status = 'prenha ou choca'
                                elif status == '3':
                                    status = 'doente'
                                lote_op = input('Para qual lote o animal deve ir?\n1-Lote para venda \n2-lote para abate \n3-lote para producao de leite e derivados \n4-reproduçao\n5-tratamento\n')
                                if lote_op == '1':
                                    lote = 'venda'
                                elif lote_op == '2':
                                    lote = 'abate'
                                elif lote_op == '3':
                                    lote = 'producao'
                                elif lote_op == '4':
                                    lote = 'reproducao'
                                elif lote_op == '5':
                                    lote = 'tratamento'
                                else:
                                    print('Lote inválido')
                                    continue
                                if status == 'prenha ou choca' and lote != 'reproducao':
                                    print('Erro: animais prenha ou choca só podem ir para o lote de reprodução')
                                    continue
                                if status == 'doente' and lote != 'tratamento':
                                    print('Erro: animais doentes devem ir para o lote de tratamento')
                                    continue
                                if status != 'doente' and lote == 'tratamento':
                                    print('Erro: apenas animais doentes devem ir para o lote de tratamento')
                                    continue
                                animal = [identificacao, status,lote]

                                existe = False
                                for a in lista:
                                    if a[0] == identificacao:
                                        existe = True
                                        break

                                if existe:
                                    print('Animal já existente')
                                else:
                                    lista.append(animal)
                                    print('Animal cadastrado')

                            elif op == '2':
                                tipo = input('----Que tipo de animal deseja encontrar---- \n'
                                            '1-bovino \n'
                                            '2-suino \n'
                                            '3-ave \n'
                                            '4-caprino \n'
                                            '5-ovino\n')

                                busca = input('Digite a identificação do animal: ')

                                if tipo == '1':
                                        lista = bovinos
                                elif tipo == '2':
                                    lista = suinos
                                elif tipo == '3':
                                    lista = aves
                                elif tipo == '4':
                                    lista = caprino
                                elif tipo == '5':
                                    lista = ovino
                                else:
                                    print('Tipo inválido')
                                    continue

                                encontrado = False
                                for a in lista:
                                    if a[0] == busca:
                                        print('Animal encontrado:', a)
                                        encontrado = True
                                        break

                                if not encontrado:
                                    print('Animal não encontrado')
                            elif op == '3':
                                atualizar = input('----Que tipo de animal deseja atualizar---- \n 1-bovino \n 2-suino \n 3-ave \n4-caprino\n5-ovino')
                                busca = input('Digite a identificação do animal: ')
                                if atualizar == '1':
                                        lista = bovinos
                                elif atualizar == '2':
                                    lista = suinos
                                elif atualizar == '3':
                                    lista = aves
                                elif atualizar == '4':
                                    lista = caprino
                                elif atualizar == '5':
                                    lista = ovino
                                else:
                                    print('Tipo inválido')
                                    continue
                                
                                encontrado = False
                                for animal in lista:
                                    if animal[0] == busca:
                                        print('Animal encontrado:', animal)
                                        novo_status = input('Qual o novo status do animal\n1-saudavel\n2-prenha ou choca\n3-doente\n ')

                                        if novo_status == '1':
                                            status = 'saudavel'
                                        elif novo_status == '2':
                                            status = 'prenha ou choca'
                                        elif novo_status == '3':
                                            status = 'doente'
                                        else:
                                            print('Status inválido')
                                            break

                                        lote_op = input('Para qual lote o animal deve ir?\n1-Lote para venda \n2-lote para abate \n3-lote para producao de leite e derivados \n4-reproduçao\n5-tratamento\n')
                                        if lote_op == '1':
                                            lote = 'venda'
                                        elif lote_op == '2':
                                            lote = 'abate'
                                        elif lote_op == '3':
                                            lote = 'producao'
                                        elif lote_op == '4':
                                            lote = 'reproducao'
                                        elif lote_op == '5':
                                            lote = 'tratamento'

                                        else:
                                            print('Lote inválido')
                                            break
                                    
                                        if status == 'prenha ou choca' and lote != 'reproducao':
                                            print('Erro: animais prenha ou choca só podem ir para o lote de reprodução')
                                            encontrado = True
                                            break
                                        if status == 'doente' and lote != 'tratamento':
                                            print('Erro: animais doentes devem ir para o lote de tratamento')
                                            encontrado = True
                                            break
                                        if status != 'doente' and lote == 'tratamento':
                                            print('Erro: apenas animais doentes devem ir para o lote de tratamento')
                                            encontrado = True
                                            break
                                        animal[1] = status
                                        animal[2] = lote

                                        print('Animal atualizado:', animal)
                                        encontrado = True
                                        break

                                if not encontrado:
                                    print('Animal não encontrado')

                            elif op == '4':
                                remover = input('----Que tipo de animal deseja remover---- \n 1-bovino \n 2-suino \n 3-ave \n4-caprino\n5-ovino')
                                busca = input('Digite a identificação do animal: ')
                                if remover == '1':
                                        lista = bovinos
                                elif remover == '2':
                                    lista = suinos
                                elif remover == '3':
                                    lista = aves
                                elif remover == '4':
                                    lista = caprino
                                elif remover == '5':
                                    lista = ovino
                                else:
                                    print('Tipo inválido')
                                    continue
                                encontrado = False
                                for animal in lista:
                                    if animal[0] == busca:
                                        print('Animal encontrado:', animal)
                                        pergunta = input('Tem certeza que deseja remover esse animal? \n 1-sim \n 2-nao \n')
                                        if pergunta == '1':
                                            lista.remove(animal)
                                            encontrado = True
                                            print('Animal removido')
                                            break
                                if not encontrado:
                                    print('Animal não encontrado')
                            elif op == '5':
                                
                                    lote_busca = input('1-Lote para venda \n 2-lote para abate \n 3-lote para produçao de leite e derivados \n 4-lote para reproduçao \n 5-lote para tratamento\n')
                                    if lote_busca == '1':
                                        nome_lote = 'venda'
                                    elif lote_busca == '2':
                                        nome_lote = 'abate'
                                    elif lote_busca == '3':
                                        nome_lote = 'producao'
                                    elif lote_busca == '4':
                                        nome_lote = 'reproducao'
                                    elif lote_busca == '5':
                                        nome_lote = 'tratamento'

                                    else:
                                        print('Lote inválido')
                                        continue
                                    print('----BOVINOS----')
                                    for a in bovinos:
                                        if a[2] == nome_lote:
                                            print(a)

                                    print('---- SUINOS ----')
                                    for a in suinos:
                                        if a[2] == nome_lote:
                                            print(a)

                                    print('---- AVES ----')
                                    for a in aves:
                                        if a[2] == nome_lote:
                                            print(a)
                                    print('---- CAPRINO ----')
                                    for a in caprino:
                                        if a[2] == nome_lote:
                                            print(a)
                                    print('---- OVINO ----')
                                    for a in ovino:
                                        if a[2] == nome_lote:
                                            print(a)
                    elif menu_adm  == '2':
                        while True:
                            op_produçao = input('\n ------O que deseja fazer?------ \n 1-Gerenciar leite e derivados \n 2-Gerenciar estoque geral \n 3-Verificar estoque geral \n 0-Retornar ao menu \n')
                            if op_produçao == '1':
                                while True:
                                    gerenciar_leite = input('\n ---Gerenciamento leite e derivados--- \n 1-Produção de leite \n 2-Produção de derivados \n 3-Historico da produção \n 0-Cancelar\n')

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
                                                    preco_derivado = float(input('Qual será o preço por Kg?'))
                                                    derivados.append([categoria, tipo, preco_derivado])
                                                elif novo_derivado == '2':
                                                    categoria = 'Iogurte'
                                                    tipo = input('Qual sabor de iogurt deseja adicionar? ')
                                                    preco_derivado = float(input('Qual sera o preço por litro? '))
                                                    derivados.append([categoria, tipo, preco_derivado])
                                                elif novo_derivado == '3':
                                                    categoria = 'Manteiga'
                                                    tipo = input('Qual tipo de manteiga deseja adicionar? ')
                                                    preco_derivado = float(input('Qual será o preço do produto? '))
                                                    derivados.append([categoria, tipo, preco_derivado])
                                                else:
                                                    print('Retornando ao menu.')

                                        
                                            elif gerenciar_derivados == '2':
                                            
                                                print('\n ----Leite disponível---- \n ', leite_disponivel, 'Litros. \n')
                                                print("Derivados registrados:")
                                                if len(derivados) == 0:
                                                    print('Nenhum derivado cadastrado.')
                                                    continue
                                                for i in range(len(derivados)):
                                                    print(f"({i+1}) {derivados[i][0]} {derivados[i][1]} | R${derivados[i][2]}")
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
                        
                            elif op_produçao == '2':
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
                                        preco_produto = float(input('Digite o preço do produto: '))
                                        
                                        # Verificar se o produto já existe
                                        existe = 0
                                        for p in produtos:
                                            if p[0] == tipo_produto and p[1] == animal:
                                                p[2] += quantidade
                                                print('Produto existente atualizado. Nova quantidade:', p[2])
                                                existe = 1
                                                break
                                        if existe == 0:
                                            produtos.append([tipo_produto, animal, quantidade, preco_produto])
                                            if animal == '':
                                                print(str(quantidade) + ' de ' + tipo_produto + ' adicionados ao estoque.')
                                            else:
                                                print(str(quantidade) + ' de ' + tipo_produto + ' (' + animal + ') adicionados ao estoque.')

                                    elif gerenciar_estoque == '2':

                                        print('\nProdutos disponíveis:')

                                        # Mostrar leite primeiro
                                        print(f"0 - Leite: {leite_disponivel} litros | R$ {preco_leite:.2f} por litro")

                                        # Mostrar produtos cadastrados
                                        for i in range(len(produtos)):
                                            if produtos[i][1] == '':
                                                print(f"{i+1} - {produtos[i][0]}: {produtos[i][2]}")
                                            else:
                                                print(f"{i+1} - {produtos[i][0]} ({produtos[i][1]}): {produtos[i][2]} | R${produtos[i][3]}")

                                        escolha = int(input('Digite o número do produto que deseja atualizar (0 = leite / -1 cancelar): '))

                                        if escolha == -1:
                                            continue

                                        if escolha == 0:

                                            print('\n--- Atualização do Leite ---')

                                            novo_preco = float(input('Digite o novo preço por litro: R$ '))
                                            preco_leite = novo_preco

                                            acao = input('Digite 1 para adicionar litros ou 2 para remover litros: ')

                                            if acao == '1':
                                                qtd = float(input('Quantos litros deseja adicionar? '))
                                                leite_disponivel += qtd
                                                print('Leite atualizado com sucesso.')

                                            elif acao == '2':
                                                qtd = float(input('Quantos litros deseja remover? '))

                                                if qtd > leite_disponivel:
                                                    print('Quantidade inválida.')
                                                else:
                                                    leite_disponivel -= qtd
                                                    print('Leite atualizado com sucesso.')

                                            else:
                                                print('Ação inválida.')

                                        else:

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

                            elif op_produçao == '3':
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
                            
                            elif op_produçao == '0':
                                break
                    elif menu_adm == '3':
                        while True:
                            financeiro = input('----Gerenciamento Financeiro---- \n 1-registrar receita \n 2-registrar despesa \n 3-ver saldo\n 4-relatorio financeiro\n 0-voltar\n')
                            if financeiro == '1':
                                descricao = input('Digite a descrição da receita: ')
                                valor = float(input('Digite o valor da receita: '))
                                data = input('Digite a data da receita (DD/MM/AAAA): ')
                                receitas.append([descricao, valor, data])
                                saldo += valor
                                print('Receita registrada com sucesso.')
                            elif financeiro == '2':
                                descricao = input('Digite a descrição da despesa: ')
                                valor = float(input('Digite o valor da despesa: '))
                                data = input('Digite a data da despesa (DD/MM/AAAA): ')
                                despesas.append([descricao, valor, data])
                                saldo -= valor
                                print('Despesa registrada com sucesso.')
                            elif financeiro == '3':
                                print('saldo atual: R$', saldo)
                            elif financeiro == '4':
                                print('----RELATÓRIO FINANCEIRO----')
                                print('----Receitas----')
                                for r in receitas:
                                    print(f'{r[0]} - R$ {r[1]} - {r[2]}')
                                print('----Despesas----')
                                for d in despesas:
                                    print(f'{d[0]} - R$ {d[1]} - {d[2]}')
                            elif financeiro == '0':
                                break
            else:
                print('senha invalida')
                   
        elif ml == 2:
            id = input('Digite o nome de usuario: ')
            senha = input('Digite sua senha: ')
            if id in user_c:
                i = user_c.index(id)
                if senha == password_c[i]:
                    print(f'Bem vindo {id}')
                    while True:
                        menu_cliente = input('----Menu Cliente----\n 1-visulizar estoque disponivel \n 2-realizar compra\n 3-agendar transporte\n')
                        if menu_cliente == '1':
                            while True:
                                opv_estoque = input('\n ----ESTOQUE DISPONIVEL---- \n 1-Leite e derivados \n 2-Animais \n 3-Produtos \n 0-Retornar ao menu \n')
                                if opv_estoque == '1':
                                    print('\n----- ESTOQUE DISPONÍVEL -----\n')
                                    print(f'Leite disponível: \n {leite_disponivel} litros | R$ {preco_leite} \n')

                                    print('DERIVADOS DISPONIVEIS: \n') 
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

                                if opv_estoque == '2':
                                    print('\n----ANIMAIS DISPONIVEIS----\n')
                                    print('----BOVINOS----')
                                    encontrado = False
                                    for animal in bovinos:
                                        if animal[2] == 'venda':
                                            print(f'ID: {animal[0]} | Status: {animal[1]}')
                                            encontrado = True

                                    if encontrado == False:
                                        print('Nenhum bovino disponível')

                                    print('\n----SUINOS----')
                                    encontrado = False

                                    for animal in suinos:
                                        if animal[2] == 'venda':
                                            print(f'ID: {animal[0]} | Status: {animal[1]}')
                                            encontrado = True

                                    if encontrado == False:
                                        print('Nenhum suíno disponível')

                                    print('\n----AVES----')
                                    encontrado = False

                                    for animal in aves:
                                        if animal[2] == 'venda':
                                            print(f'ID: {animal[0]} | Status: {animal[1]}')
                                            encontrado = True

                                    if encontrado == False:
                                        print('Nenhuma ave disponível')

                                    print('\n----CAPRINOS----')
                                    encontrado = False

                                    for animal in caprino:
                                        if animal[2] == 'venda':
                                            print(f'ID: {animal[0]} | Status: {animal[1]}')
                                            encontrado = True

                                    if encontrado == False:
                                        print('Nenhum caprino disponível')

                                    print('\n----OVINOS----')
                                    encontrado = False

                                    for animal in ovino:
                                        if animal[2] == 'venda':
                                            print(f'ID: {animal[0]} | Status: {animal[1]}')
                                            encontrado = True

                                    if encontrado == False:
                                        print('Nenhum ovino disponível')

                                if opv_estoque == '3':
                                    print('----PRODUTOS DISPONIVEIS----')  
                                    if len(produtos) == 0:
                                        print('Nenhum produto disponivel.')
                                    else:
                                        for i in range(len(produtos)):
                                            if produtos[i][1] == '':
                                                print(f'{produtos[i][0]}: {produtos[i][2]} disponíveis | R$ {produtos[i][3]}')
                                            else:
                                                print(f'{p[0]} ({p[1]}): {p[2]} disponíveis | R$ {p[3]}')    

                                if opv_estoque == '0':
                                    break    

                        elif menu_cliente == '2':
                            while True:
                                compra = input(' \n ----MENU COMPRAS---- \n 1-Leite e derivados \n 2-animais \n 2-Produtos \n')
                                if compra == '1':
                                    compra_lderivados = input(' \n ----O que deseja comprar? ---- \n 1-Leite \n 2-Derivados \n 0-Cancelar \n')
                                    if compra_lderivados == '1':
                                        print(f'Leite disponível: \n {leite_disponivel} litros | R$ {preco_leite} \n')
                                        compra_leite = int(input('Quantos litros de leite deseja comprar? '))
                                        total_cleite = compra_leite * preco_leite
                                        leite_disponivel = leite_disponivel - compra_leite
                                        print(f'Compra realizada com sucesso. \n Leite comprado: {compra_leite} | R${total_cleite}')
                                    
                                    elif compra_lderivados == '2':
                                        print('DERIVADOS DISPONIVEIS: \n') 
                                        if len(producao_derivados) == 0:
                                            print("Nenhum derivado produzido ainda.")
                                        else:
                                            print("Derivados disponíveis:")
                                            for item in producao_derivados:
                                                if item[0] == 'Iogurte':
                                                    unidade = 'L'
                                                else:
                                                    unidade = 'kg'
                                                print(f"({i + 1}){item[0]} {item[1]}: {item[2]} {unidade}") 
                                        
                                        escolha_derivado = int(input('Qual derivado deseja comprar? '))
                                        item = producao_derivados[escolha_derivado]

                                        print(f"\nVocê escolheu: {item[0]} {item[1]}")
                                        print(f"Estoque disponível: {item[2]}")
                                        quantidade = float(input("Quantos deseja comprar? "))
                                        if quantidade > item[2]:
                                            print("Estoque insuficiente.")
                                        else:
                                            item[2] -= quantidade
                                            print("Compra realizada com sucesso!")
                                        
                                                                                                                                                                                     
                                if compra == '2':
                                    compra_animal = input('que tipo de animal deseja comprar?\n1-bovino \n 2-suino \n 3-ave \n4-caprino\n5-ovino\n')
                                    quantidade_animal = int(input('quantos animais deseja comprar?\n'))
                                    dia_compra = input('data da compra: ')
                                    if compra_animal == '1':
                                        lista = bovinos
                                        tipo_nome = 'bovino'
                                        preco_animal = 3500
                                    elif compra_animal == '2':
                                        lista = suinos
                                        preco_animal = 700
                                        tipo_nome = 'suino'
                                    elif compra_animal == '3':
                                        lista = aves
                                        preco_animal = 75
                                        tipo_nome = 'ave'
                                    elif compra_animal == '4':
                                        lista = caprino
                                        preco_animal = 500
                                        tipo_nome = 'caprino'
                                    elif compra_animal == '5':
                                        lista = ovino
                                        preco_animal = 500
                                        tipo_nome = 'Ovino'
                                    else:
                                        print('tipo invalido')
                                        continue
                                    disponiveis = []
                                    for animal in lista:
                                        if animal[2] == 'venda':
                                            disponiveis.append(animal)
                                    if len(disponiveis) == 0:
                                        print(f'Nenhum {tipo_nome} disponível para venda.')
                                    elif quantidade_animal > len(disponiveis):
                                        print('Quantidade indisponível.')
                                    else:
                                        preco_total = preco_animal * quantidade_animal
                                        compra_final = input(f'o preço total da compra e de R${preco_total}, deseja continuar a compra?\n1-sim\n2-nao')
                                        if compra_final == '1':
                                            vendidos = 0
                                            i = 0
                                            while i < len(lista) and vendidos < quantidade_animal:

                                                if lista[i][2] == 'venda':
                                                    print(f'Animal vendido: {lista[i][0]}')
                                                    lista.pop(i)
                                                    vendidos += 1
                                                else:
                                                    i += 1

                                            saldo += preco_total
                                            receitas.append([
                                                f'Venda de {vendidos} {tipo_nome}(s)',preco_total,dia_compra])
                                            print(f'{vendidos} animais vendidos.')
                                else:
                                    break                   
            else:
                print('senha invalida')
    elif menu == 2:
        mr = int(input('1-Registrar como ADM \n 2-Registrar como Cliente \n 0-Fechar o programa \n'))
        if mr == 1:
            id = input('Digite o nome de usuario: ')
            senha = input('Digite sua senha: ')
            if id in user_adm:
                print('Usuario ja existente')
            else:
                user_adm.append(id)
                password_adm.append(senha)
        if mr == 2:
            id = input('Digite o nome de usuario: ')
            senha = input('Digite sua senha: ')
            if id in user_c:
                print('Usuario ja existente')
            else:
                user_c.append(id)
                password_c.append(senha)

print('programa finalizado')