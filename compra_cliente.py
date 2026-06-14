from producao_leite_derivados import leite_derivados
from dados import agendamentos, clientes, historico_vendas
import datetime, tabulate

def mostrar_animais_venda(animais):

    tipos = {
        'bovino': 'BOVINOS',
        'suino': 'SUÍNOS',
        'ave': 'AVES',
        'caprino': 'CAPRINOS',
        'ovino': 'OVINOS'
    }
    print('\n----ANIMAIS DISPONÍVEIS----\n')

    for tipo, titulo in tipos.items():
        print(f'----{titulo}----')
        encontrado = False
        for id_animal, dados in animais[tipo].items():
            if dados['status'] == 'venda':

                print(
                    f'ID: {id_animal} | '
                    f'Status: {dados["status"]}'
                )
                encontrado = True
        if not encontrado:
            print(f'Nenhum {tipo} disponível')

def mostrar_produtos(produtos):
    print('\n----PRODUTOS DISPONÍVEIS----')
    vazio = True
    for animal, dados in produtos['Carne'].items():
        vazio = False
        print(
            f'Carne ({animal}): '
            f'{dados["quantidade"]} disponíveis | '
            f'R$ {dados["preco"]}'
        )

    for tipo in ['Ovos', 'Lã', 'Pele', 'Banha']:
        if produtos[tipo]:
            vazio = False
            print(
                f'{tipo}: '
                f'{produtos[tipo]["quantidade"]} disponíveis | '
                f'R$ {produtos[tipo]["preco"]}'
            )
    if vazio:
        print('Nenhum produto disponível.')

def compra_leite_derivados(cliente_logado):
    compra_lderivados = input(' \n ----O que deseja comprar? ---- \n 1-Leite \n 2-Derivados \n 0-Cancelar \n')
    if compra_lderivados == '1':
        escolha_lderivados = input('O que deseja comprar? \n 1-Leite \n 2-Derivados')
        if escolha_lderivados == '1':
            if leite_derivados['leite']['preco'] == 0:
                print('Leite não disponivel para a venda.')
                return
            else:
                print(f"LEITE DISPONÍVEL: {leite_derivados['leite']['disponivel']} Litros\nPreço: R${leite_derivados['leite']['preco']}")
                quantia_leite = float(input('Quantos litros de leite deseja comprar? '))
                if quantia_leite <= 0 or quantia_leite > leite_derivados['leite']['disponivel']:
                    print('Quantia indisponivel.')
                    return
                else: 
                    valor_total = quantia_leite * leite_derivados['leite']['preco']
                    print(f'O valor total foi de: R${valor_total}')
                    confirmacao = input('deseja realizar a compra? (s/n)')
                    if confirmacao == 's':
                       valor_total = quantia_leite * leite_derivados['leite']['preco']
                       leite_derivados['leite']['disponivel'] -= quantia_leite
                       historico_vendas.append({
                       'data': datetime.date.today().strftime("%d/%m/%Y"),
                       'produto': 'Leite',
                       'quantidade': quantia_leite,
                       'valor': valor_total,
                       'cliente': cliente_logado,
                       'status': 'Ativa'
                        })
                       print('Compra realizada com sucesso.')
                    elif confirmacao == 'n':
                        print('Compra cancelada') 
                    else:
                        print('Escolha invalida.')
                        return
                    
        elif escolha_lderivados == '2':
            if leite_derivados['derivados'] == []:
                print('Nenhum derivado disponivel.')
            else:
                print('\n ----DERIVADOS DISPONIVEIS---- \n')
                i = 0
                for d in leite_derivados['derivados']:
                    print(f'({i+1}) - {d["derivado"]}')
                    i += 1
                escolha = int(input('Qual derivado deseja comprar?(numero): ')) - 1
                if escolha < 0 or escolha >= len(leite_derivados['derivados']):
                    print('Opção inválida.')
                    return
                derivado_escolhido = leite_derivados['derivados'][escolha]
                if derivado_escolhido['tipos'] == []:
                    print('Esse derivado não possui tipos cadastrados.')
                    return
            tipos_disponiveis = []
            i = 0
            for t in derivado_escolhido['tipos']:
                if t['preco'] > 0 and t['estoque'] > 0:
                    print(f'({i+1}) | {t["tipo"]} | ({t["estoque"]} disponíveis)')
                    tipos_disponiveis.append(t)
                    i += 1
            if len(tipos_disponiveis) == 0:
                print('Nenhum tipo disponível para venda.')
                return
            escolha_tipo = int(input('Qual tipo deseja escolher?(numero) ')) - 1
            if escolha_tipo < 0 or escolha_tipo >= len(tipos_disponiveis):
                print('Tipo inválido.')
                return
            tipo = tipos_disponiveis[escolha_tipo]
            quantidade = float(input('Quantos Kg/L deseja comprar? '))
            if quantidade <= 0 or quantidade > tipo['estoque']:
                print('Quantia indisponivel.')
            else:
                valor_total = quantidade * tipo['preco']
                print(f'O total da compra sera: R${valor_total}')
                confirmacao = input('Deseja finalizar a compra? (s/n)')
                if confirmacao == 's':
                    tipo['estoque'] -= quantidade
                    historico_vendas.append({
                    'data': datetime.date.today().strftime("%d/%m/%Y"),
                    'produto': f"{derivado_escolhido['derivado']} - {tipo['tipo']}",
                    'quantidade': quantidade,
                    'valor': valor_total,
                    'cliente': cliente_logado,
                    'status': 'Ativa'
                    })    
                    print('Compra realizada com sucesso.')
                elif confirmacao == 'n':
                    print('Compra cancelada') 
                else:
                    print('Escolha invalida.')
                    return

def mostrar_produtos_comprados(cliente):
    compras_cliente = []
    for compra in historico_vendas:
        if compra['cliente'] == cliente:
            compras_cliente.append(compra)
    if len(compras_cliente) == 0:
        print('Nenhuma compra encontrada.')
        return []
    tabela = []
    for i, compra in enumerate(compras_cliente):
        tabela.append([i + 1, compra['produto'], compra['quantidade'], f'R${compra["valor"]}'])
    print(tabulate(
        tabela,
        headers=['Nº', 'Produto', 'Quantidade', 'Valor'],
        tablefmt='grid'
    ))
    return compras_cliente

def agendar_retirada(cliente_logado):

    if clientes[cliente_logado]['telefone'] is None:
        telefone = input('Digite seu telefone para contato: ')
        clientes[cliente_logado]['telefone'] = telefone
    compras_cliente = mostrar_produtos_comprados(cliente_logado)
    if len(compras_cliente) == 0:
        return
    escolha = int(input('\nQual compra deseja retirar? ')) - 1
    if escolha < 0 or escolha >= len(compras_cliente):
        print('Opção inválida.')
        return
    compra_escolhida = compras_cliente[escolha]
    data_retirada = input('Digite a data da retirada (dd/mm/aaaa): ')
    hora_retirada = input('Digite o horário da retirada: ')

    agendamentos.append({
        'cliente': cliente_logado,
        'telefone': clientes[cliente_logado]['telefone'],
        'data_agendamento': datetime.date.today().strftime("%d/%m/%Y"),
        'produto': compra_escolhida['produto'],
        'quantidade': compra_escolhida['quantidade'],
        'valor': compra_escolhida['valor'],
        'data_retirada': data_retirada,
        'hora': hora_retirada
    })
    print('\nRetirada agendada com sucesso!')

def ver_agendamentos_adm(cliente):
    tabela = []
    for agendamento in agendamentos:
        if agendamento['cliente'] == cliente:
            telefone = agendamento['telefone']
            telefone_formatado = (
                f'({telefone[:2]}) '
                f'{telefone[2]} '
                f'{telefone[3:7]}-{telefone[7:]}'
            )
            tabela.append([
                agendamento['data_agendamento'],
                agendamento['produto'],
                agendamento['quantidade'],
                f'R${agendamento["valor"]}',
                agendamento['data_retirada'],
                telefone_formatado
            ])
    if len(tabela) == 0:
        print('Nenhum agendamento encontrado.')
        return
    print(tabulate(
        tabela,
        headers=['Agendado em','Produto','Qtd','Valor','Retirada','Telefone'],
        tablefmt='grid'
    ))    

def solicitar_reembolso(cliente_logado):
    compras_cliente = mostrar_produtos_comprados(cliente_logado)
    if len(compras_cliente) == 0:
        return
    escolha = int(input('\nQual compra deseja reembolsar? ')) - 1
    if escolha < 0 or escolha >= len(compras_cliente):
        print('Opção inválida.')
        return
    
    compra = compras_cliente[escolha]
    if compra['status'] == 'Reembolsada':
        print('Essa compra já foi reembolsada.')
        return
    
    confirmacao = input(f'Deseja reembolsar "{compra["produto"]}"? (s/n) ')
    if confirmacao != 's':
        print('Operação cancelada.')
        return
    
    compra['status'] = 'Reembolsada'
    for agendamento in agendamentos[:]:
        if agendamento['cliente'] == cliente_logado:
            if agendamento['produto'] == compra['produto']:
                agendamentos.remove(agendamento)
    if compra['produto'] == 'Leite':
        leite_derivados['leite']['disponivel'] += compra['quantidade']
    else:
        for derivado in leite_derivados['derivados']:
            for tipo in derivado['tipos']:
                nome_produto = (derivado['derivado']+ ' - ' + tipo['tipo'])
                if nome_produto == compra['produto']:
                    tipo['estoque'] += compra['quantidade']
    print('Reembolso realizado com sucesso!')

def gerenciar_precos():
    print('\n1 - Alterar preço do leite \n 2 - Alterar preço de derivado')
    escolha = input('Escolha: ')
    if escolha == '1':
        print(f'Preço atual: R${leite_derivados["leite"]["preco"]}')
        leite_derivados['leite']['preco'] = float(input('Novo preço: '))
        print('Preço atualizado.')

    elif escolha == '2':
        i = 0
        for derivado in leite_derivados['derivados']:
            print(f'({i+1}) - {derivado["derivado"]}')
            i += 1
        escolha_derivado = int(input('Escolha o derivado: ')) - 1
        if escolha_derivado < 0 or escolha_derivado >= len(leite_derivados['derivados']):
            print('Opção inválida.')
            return
        derivado = leite_derivados['derivados'][escolha_derivado]
        i = 0
        for tipo in derivado['tipos']:
            print(f'({i+1}) - {tipo["tipo"]}')
            i += 1
        escolha_tipo = int(input('Escolha o tipo: ')) - 1
        if escolha_tipo < 0 or escolha_tipo >= len(derivado['tipos']):
            print('Tipo inválido.')
            return
        tipo = derivado['tipos'][escolha_tipo]
        print(f'Preço atual: R${tipo["preco"]}')
        tipo['preco'] = float(input('Novo preço: '))
        print('Preço atualizado.')