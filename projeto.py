from autenticacao import login_adm, login_cliente, registrar_adm, registrar_cliente
from rebanho import cadastrar_animal, buscar_animal,atualizar_animal,remover_animal,gerenciar_lotes
from financeiro import registrar_despesas,registrar_receita,relatorio_financeiro,ver_saldo
from producao import producao_leite,produzir_derivado,estoque_LeiteDerivados,cadastrar_tipo_derivado, cadastrar_derivado, leite_derivados
from estoque import registrar_produto,ver_estoque
from dados import produtos,animais
from gerenciar_maquinas import registrar_maquina, status_maquina, remover_maquina, maquinas_indisponiveis
from cliente_compra import mostrar_animais_venda, mostrar_produtos, compra_leite_derivados, compra_animal, agendar_retirada, mostrar_produtos_comprados, solicitar_reembolso,compra_produtos, gerenciar_precos_leitederivados
from graficos import grafico_faturamento, grafico_producao_leite, grafico_vendas_leite_derivados

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
                    menu_adm = input('----Menu ADM----\n 1-gerenciar rebanho\n 2-gerenciar produçao e derivados\n 3-gerenciamento financeiro\n 4-Gerenciar Maquinas \n')
                    
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
                                    gerenciar_leite = input('\n ---Gerenciamento leite e derivados--- \n 1-Produção de leite \n 2-Produção de derivados \n 3-Grafico de vendas e produção \n 4-Gerenciar preços \n 0-Cancelar\n')
                                    if gerenciar_leite == '1':
                                       producao_leite()

                                    elif gerenciar_leite == '2':
                                        while True:
                                            gerenciar_derivados = input('\n ----Gerenciar derivados---- \n 1-Registrar derivado \n 2- Registrar tipo de derivado \n 3-Produzir derivado \n 4-Status de produção \n 0-Cancelar \n ')
                                            if gerenciar_derivados == '1':
                                                cadastrar_derivado()
                                            elif gerenciar_derivados == '2':
                                                cadastrar_tipo_derivado()
                                            elif gerenciar_derivados == '3':
                                                produzir_derivado()
                                            elif gerenciar_derivados == '4':
                                                estoque_LeiteDerivados()                                            
                                            elif gerenciar_derivados == '0':
                                                break
                                            else:
                                                print('Opção inválida.')

                                    elif gerenciar_leite == '3':
                                        graficos = input('-----GRAFICOS-----\n 1-Produção de leite \n 2-Vendas \n 3-Faturamento \n 0-Cancelar \n')
                                        if graficos == '1':
                                            grafico_producao_leite(leite_derivados)
                                        elif graficos == '2':
                                            grafico_vendas_leite_derivados(0)
                                        elif graficos == '3':
                                            grafico_faturamento()
                                    elif gerenciar_leite == '4':
                                        gerenciar_precos_leitederivados()
                                    elif gerenciar_leite == '0':
                                        break     
                                    else:
                                        print('Validação Invalida')                       
                        
                            elif op_produçao == '2':
                                while True:
                                    gerenciar_estoque = input('\n----Gerenciamento de estoque----\n 1-Gerenciar produto do rebanho\n2-Atualizar estoque\n 0-Cancelar\n') 
                                    if gerenciar_estoque == '1':
                                        registrar_produto(produtos)
                                    elif gerenciar_estoque == '2':
                                        gerenciar_precos_leitederivados()
                                    else:
                                        break
                            elif op_produçao == '3':
                                ver_estoque()
                            
                            else:
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
                            else:
                                break

                    elif menu_adm == '4':
                        while True:
                            maquina = input('----GERENCIAR MAQUINAS---- \n 1-Registrar maquina \n 2-Status maquina \n 3-Remover maquina \n 4-Checar maquinas indisponiveis \n 0-Cancelar\n ')
                            if maquina == '1':
                                registrar_maquina()
                            elif maquina == '2':
                                status_maquina()
                            elif maquina == '3':
                                remover_maquina()
                            elif maquina == '4':
                                maquinas_indisponiveis()
                            elif maquina == '4':
                                break
                            else:
                                print('Por favor selecione uma opção valida')
                                continue

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
                                    estoque_LeiteDerivados()
                                elif opv_estoque == '2':
                                    mostrar_animais_venda(animais)
                                elif opv_estoque == '3':
                                    mostrar_produtos(produtos)
                                elif opv_estoque == '0':
                                    break

                        elif menu_cliente == '2':
                            while True:
                                compra = input(' \n ----MENU COMPRAS---- \n 1-Leite e derivados \n 2-Animais \n 3-Produtos \n 0-Voltar \n ')
                                if compra == '1':
                                    compra_leite_derivados(usuario)

                                elif compra == '2':
                                    compra_animal(usuario, animais)

                                elif compra == '3':
                                    compra_produtos(usuario, produtos)

                                elif compra == '0':
                                    break
                        elif menu_cliente == '3':
                            while True:
                                menu_agendamento = input('\n ----AGENDAR RETIRADA---- \n 1-Agendar retirada \n 2-Ver agendamentos \n 3-Solicitar reembolso \n 0-Retornar ao menu \n')
                                if menu_agendamento == '1':
                                    agendar_retirada(usuario)
                                elif menu_agendamento == '2':
                                    from cliente_compra import ver_agendamentos_adm
                                    ver_agendamentos_adm(usuario)
                                elif menu_agendamento == '3':
                                    solicitar_reembolso(usuario)
                                elif menu_agendamento == '0':
                                    break
                        elif menu_cliente =='4':
                            mostrar_produtos_comprados(usuario)
    elif menu == '2':
        mr = int(input('1-Registrar como ADM \n 2-Registrar como Cliente \n 0-Fechar o programa \n'))
        if mr == 1:
            registrar_adm()
        if mr == 2:
            registrar_cliente()

    else:
        print('programa finalizado')
        break