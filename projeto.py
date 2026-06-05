from autenticacao import login_adm, login_cliente, registrar_adm, registrar_cliente
from rebanho import cadastrar_animal, buscar_animal,atualizar_animal,remover_animal,gerenciar_lotes
from financeiro import registrar_despesas,registrar_receita,relatorio_financeiro,ver_saldo
from producao import producao_leite,produzir_derivado,estoque_LeiteDerivados,registrar_derivado
from estoque import atualizar_preco,registrar_produto,ver_estoque
from dados import produtos,leite_derivados,animais
from cliente_compra import mostrar_leite_derivados,mostrar_animais_venda,mostrar_produtos
producao_derivados = []
leite_disponivel = 0
preco_leite = 0

agendamentos = []
saldo = 0
op = -99
index = -99
menu = '-99'

while menu != 0:
    menu = (input('----MENU---- \n 1-Fazer login \n 2-Registrar \n 0-Fechar o programa \n'))
    if menu == '1':
        ml = (input('1-Fazer login como ADM \n 2-fazer login como Cliente \n 0-Fechar o programa \n'))
        if ml == '1':
            usuario = login_adm()
            if usuario is not None:
                    menu_adm = input('----Menu ADM----\n1-gerenciar rebanho\n 2-gerenciar produçao e derivados\n 3-gerenciamento financeiro\n')
                    if menu_adm == '1':
                        op = '-99'
                        while op != '0':
                            op = input('------O que deseja fazer?------ \n 1-Cadastrar Animal \n 2-Buscar Animal \n 3-Atualizar Rebanho \n 4-Remover \n 5-gerenciamento de lotes \n 0-retornar ao menu \n')
                            if op == '1':
                                cadastrar_animal()

                            elif op == '2':
                                buscar_animal()

                            elif op == '3':
                                atualizar_animal()

                            elif op == '4':
                                remover_animal()

                            elif op == '5':
                                gerenciar_lotes()
                    elif menu_adm  == '2':
                        while True:
                            op_produçao = input('\n ------O que deseja fazer?------ \n 1-Gerenciar leite e derivados \n 2-Gerenciar estoque geral \n 3-Verificar estoque geral \n 0-Retornar ao menu \n')
                            if op_produçao == '1':
                                while True:
                                    gerenciar_leite = input('\n ---Gerenciamento leite e derivados--- \n 1-Produção de leite \n 2-Produção de derivados \n 0-Cancelar\n')

                                    if gerenciar_leite == '1':
                                       producao_leite()
                                    
                                    elif gerenciar_leite == '2':
                                        while True:
                                            gerenciar_derivados = input('\n ----Gerenciar derivados---- \n 1-Registrar derivado \n 2-Produzir derivado \n 3-Status de produção \n 0-Cancelar \n ')

                                            if gerenciar_derivados == '1':
                                                registrar_derivado()

                                            elif gerenciar_derivados == '2':
                                                produzir_derivado()

                                            elif gerenciar_derivados == '3':
                                                estoque_LeiteDerivados()
                                            
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
                                    gerenciar_estoque = input('\n----Gerenciamento de estoque----\n1-Gerenciar produto do rebanho\n2-Atualizar estoque\n0-Cancelar\n') 
                                    if gerenciar_estoque == '1':
                                        registrar_produto(produtos)

                                    elif gerenciar_estoque == '2':
                                        atualizar_preco()

                            elif op_produçao == '3':
                                ver_estoque(leite_derivados, produtos)

                            elif op_produçao == '0':
                                break
                    elif menu_adm == '3':
                        while True:
                            financeiro = input('----Gerenciamento Financeiro---- \n 1-registrar receita \n 2-registrar despesa \n 3-ver saldo\n 4-relatorio financeiro\n 0-voltar\n')
                            if financeiro == '1':
                                registrar_receita()
                            elif financeiro == '2':
                                registrar_despesas()
                            elif financeiro == '3':
                                ver_saldo()
                            elif financeiro == '4':
                                relatorio_financeiro()
                   
        elif ml == '2':
            usuario = login_cliente()
            if usuario is not None:
                    historico = []
                    avaliaçoes = []
                    while True:
                        menu_cliente = input('----Menu Cliente----\n 1-visulizar estoque disponivel \n 2-realizar compra\n 3-agendar transporte\n 4-historico de compra\n')
                        if menu_cliente == '1':
                            while True:
                                opv_estoque = input('\n ----ESTOQUE DISPONIVEL---- \n 1-Leite e derivados \n 2-Animais \n 3-Produtos \n 0-Retornar ao menu \n')
                                if opv_estoque == '1':
                                 mostrar_leite_derivados(leite_derivados, preco_leite)

                                if opv_estoque == '2':
                                   mostrar_animais_venda(animais)
                                if opv_estoque == '3':
                                    mostrar_produtos(produtos) 

                                if opv_estoque == '0':
                                    break    

                        elif menu_cliente == '2':
                            while True:
                                compra = input(' \n ----MENU COMPRAS---- \n 1-Leite e derivados \n 2-animais \n 3-Produtos \n ')
                                if compra == '1':
                                    compra_lderivados = input(' \n ----O que deseja comprar? ---- \n 1-Leite \n 2-Derivados \n 0-Cancelar \n')
                                    if compra_lderivados == '1':
                                        print(f'Leite disponível: \n {leite_disponivel} litros | R$ {preco_leite} \n')
                                        compra_leite = int(input('Quantos litros de leite deseja comprar? '))
                                        if compra_leite > leite_disponivel:
                                            print('Quantia indisponivel.')
                                        else:    
                                            total_cleite = compra_leite * preco_leite
                                            leite_disponivel = leite_disponivel - compra_leite
                                            print(f'Compra realizada com sucesso. \n Leite comprado: {compra_leite} | R${total_cleite}')
                                            historico.append([id, 'Leite', compra_leite, total_cleite])
                                    
                                    elif compra_lderivados == '2':
                                        print('DERIVADOS DISPONIVEIS: \n') 
                                        if len(producao_derivados) == 0:
                                            print("Nenhum derivado produzido ainda.")
                                        else:
                                            print("Derivados disponíveis:")
                                            for i in range(len(producao_derivados)):
                                                item = producao_derivados[i]
                                                if item[0] == 'Iogurte':
                                                    unidade = 'L'
                                                else:
                                                    unidade = 'kg'
                                                print(f"({i + 1}){item[0]} {item[1]}: {item[2]} {unidade}") 
                                        
                                        escolha_derivado = int(input('Qual derivado deseja comprar? '))
                                        item = producao_derivados[escolha_derivado - 1]

                                        print(f"\nVocê escolheu: {item[0]} {item[1]}")
                                        print(f"Estoque disponível: {item[2]}")
                                        quantidade = float(input("Quantos deseja comprar? "))
                                        if quantidade > item[2]:
                                            print("Estoque insuficiente.")
                                        else:
                                            preco = item[3]
                                            total = quantidade * preco
                                            item[2] -= quantidade
                                            print(f"Compra realizada com sucesso! \n Quantia comprada: {quantidade} | R${total}")
                                            historico.append([id,f'{item[0]} {item[1]}',quantidade,total])
                                        
                                                                                                                                                                                     
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
                                            receita.append([
                                                f'Venda de {vendidos} {tipo_nome}(s)',preco_total,dia_compra])
                                            print(f'{vendidos} animais vendidos.')
                                            historico.append([id,tipo_nome,vendidos,preco_total])
                                
                                elif compra == '3':
                                    print('----PRODUTOS DISPONIVEIS----')  
                                    if len(produtos) == 0:
                                        print('Nenhum produto disponivel.')
                                    else:
                                        for i in range(len(produtos)):
                                            if produtos[i][1] == '':
                                                print(f'{produtos[i][0]}: {produtos[i][2]} disponíveis | R$ {produtos[i][3]}')
                                            else:
                                                print(f'{produtos[i][0]} ({produtos[i][1]}): {produtos[i][2]} disponíveis | R$ {produtos[i][3]}') 

                                    compra_produto = int(input('Qual produto deseja comprar? '))
                                    if compra_produto < 1 or compra_produto > len(produtos):                                        
                                        print('Produto indisponivel.')
                                    else:
                                        quantia_produto = float(input('Quanto deseja comprar? '))
                                        produto = produtos[compra_produto - 1]
                                        if quantia_produto < 1 or quantia_produto > produto[2]:
                                            print('Quantia indisponivel.')
                                        else:
                                            produto[2] -= quantia_produto
                                            preco_total = produto[3] * quantia_produto
                                            print(f'Compra realizada com sucesso. \n Quantia adquirida: {quantia_produto} | R${preco_total}')
                                            saldo += preco_total
                                            historico.append([id,produto[0],quantia_produto,preco_total])
                                else:
                                    break     
                        elif menu_cliente == '3':
                            while True:
                                menu_agendamento = input('\n ----AGENDAR TRANSPORTE---- \n 1-Agendar retirada \n 2-Ver agendamentos \n 3-Cancelar agendamento \n 0-Retornar ao menu \n')

                                if menu_agendamento == '1':
                                    dia_retirada = input('Informe o dia que sera feito a retirada: ')
                                    horario_retirada = input('Informe o horario da retirada: ')
                                    agendamentos.append([dia_retirada, horario_retirada])
                                    print('Agendamento feito com sucesso.')

                                if menu_agendamento == '2':
                                    print('----AGENDAMENTOS EM ANDAMENTO----')
                                    for a in range(len(agendamentos)):
                                        print(f'dia: {agendamentos[a][0]} | horario: {agendamentos[a][1]}')

                                if menu_agendamento == '3':
                                    print('----CANCELAR AGENDAMENTO----')
                                    if len(agendamentos) == 0:
                                        print('Nenhum agendamento em andamento.')
                                    else:    
                                        for a in range(len(agendamentos)):
                                            print(f'({a+1}) dia: {agendamentos[a][0]} | horario: {agendamentos[a][1]}')
                                        excluir_agendamento = int(input('Digite o agendamento que deseja cancelar: '))
                                        if excluir_agendamento < 1 or excluir_agendamento > len(agendamentos):
                                            print('Agendamento não encontrado.')
                                        else:
                                            agendamentos.pop(excluir_agendamento - 1)
                                            print('Agendamento cancelado com sucesso.')

                                if menu_agendamento == '0':
                                    break            
                        elif menu_cliente =='4':
                            print('----HISTORICO DE COMPRAS----')
                            encontrou = False
                            for h in historico:
                                if h[0] == id:
                                    print(f'Produto: {h[1]}')
                                    print(f'Quantidade: {h[2]}')
                                    print(f'Valor total: R$ {h[3]}')
                                    print('-------------------')
                                    encontrou = True
                            if encontrou == False:
                                print('Nenhuma compra encontrada.')
    elif menu == '2':
        mr = int(input('1-Registrar como ADM \n 2-Registrar como Cliente \n 0-Fechar o programa \n'))
        if mr == 1:
            registrar_adm()
        if mr == 2:
            registrar_cliente()

    else:
        print('programa finalizado')
        break