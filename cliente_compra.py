from producao import leite_derivados
from dados import agendamentos, clientes, historico_vendas, animais
import datetime
from tabulate import tabulate

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
            if dados['lote'] == 'venda':

                print(
                    f'ID: {id_animal} | '
                    f'Status: {dados["status"]} | '
                    f'Lote: {dados["lote"]}'
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
    if compra_lderivados == '0':
        return
    elif compra_lderivados == '1':
        if leite_derivados['leite']['preco'] == 0:
            print('Leite não disponivel para a venda.')
            return
        print(f"LEITE DISPONÍVEL: {leite_derivados['leite']['disponivel']} Litros\nPreço: R${leite_derivados['leite']['preco']}")
        quantia_leite = float(input('Quantos litros de leite deseja comprar? '))
        if quantia_leite <= 0 or quantia_leite > leite_derivados['leite']['disponivel']:
            print('Quantia indisponivel.')
            return
        valor_total = quantia_leite * leite_derivados['leite']['preco']
        print(f'O valor total foi de: R${valor_total:.2f}')
        confirmacao = input('Deseja realizar a compra? (s/n) ')
        if confirmacao == 's':
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
            print('Compra cancelada.')
        else:
            print('Escolha inválida.')

    elif compra_lderivados == '2':
        if leite_derivados['derivados'] == []:
            print('Nenhum derivado disponivel.')
            return
        print('\n ----DERIVADOS DISPONIVEIS---- \n')
        for i, d in enumerate(leite_derivados['derivados']):
            print(f'({i+1}) - {d["derivado"]}')
        escolha = int(input('Qual derivado deseja comprar?(numero): ')) - 1
        if escolha < 0 or escolha >= len(leite_derivados['derivados']):
            print('Opção inválida.')
            return
        derivado_escolhido = leite_derivados['derivados'][escolha]
        if derivado_escolhido['tipos'] == []:
            print('Esse derivado não possui tipos cadastrados.')
            return
        for i, t in enumerate(derivado_escolhido['tipos']):
            print(f'({i+1}) {t["tipo"]} | Estoque: {t["estoque"]} | R${t["preco"]}')
        escolha_tipo = int(input('Qual tipo deseja escolher?(numero) ')) - 1
        if escolha_tipo < 0 or escolha_tipo >= len(derivado_escolhido['tipos']):
            print('Tipo inválido.')
            return
        tipo = derivado_escolhido['tipos'][escolha_tipo]
        if tipo['preco'] == 0:
            print('Este derivado não está disponível para venda.')
            return
        quantidade = float(input('Quantos Kg/L deseja comprar? '))
        if quantidade <= 0 or quantidade > tipo['estoque']:
            print('Quantia indisponivel.')
            return
        valor_total = quantidade * tipo['preco']
        print(f'O total da compra será: R${valor_total:.2f}')
        confirmacao = input('Deseja finalizar a compra? (s/n) ')
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
            print('Compra cancelada.')
        else:
            print('Escolha inválida.')
    else:
        print('Opção inválida.')

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

def compra_animal(usuario, animais):
    preco_map = {'bovino': 3500.0, 'suino': 700.0, 'ave': 75.0, 'caprino': 500.0, 'ovino': 500.0}
    tipo_map = {'1':'bovino','2':'suino','3':'ave','4':'caprino','5':'ovino'}

    compra_animal_op = input('Que tipo de animal deseja comprar?\n1-bovino\n2-suino\n3-ave\n4-caprino\n5-ovino\n')
    tipo_nome = tipo_map.get(compra_animal_op)
    if tipo_nome is None:
        print('Tipo inválido.')
        return

    disponiveis = {id_a: d for id_a, d in animais[tipo_nome].items() if d['lote'] == 'venda'}
    if len(disponiveis) == 0:
        print(f'Nenhum {tipo_nome} disponível para venda.')
        return

    preco_animal = preco_map[tipo_nome]
    print(f'\n----{tipo_nome.upper()}S DISPONÍVEIS PARA VENDA----')
    print(f'Preço por animal: R${preco_animal:.2f}')
    for id_a, d in disponiveis.items():
        print(f'  ID: {id_a} | Status: {d["status"]}')

    quantidade_animal = int(input('Quantos animais deseja comprar? '))
    if quantidade_animal <= 0 or quantidade_animal > len(disponiveis):
        print('Quantidade indisponível.')
        return

    preco_total = preco_animal * quantidade_animal
    confirmacao = input(f'O preço total é R${preco_total:.2f}. Confirma a compra?\n1-Sim\n2-Não\n')
    if confirmacao != '1':
        print('Compra cancelada.')
        return

    ids_para_remover = list(disponiveis.keys())[:quantidade_animal]
    for id_a in ids_para_remover:
        print(f'Animal vendido: {id_a}')
        del animais[tipo_nome][id_a]

    from dados import financeiro as fin
    fin['saldo'] += preco_total
    print(f'{quantidade_animal} animal(is) vendido(s). Total: R${preco_total:.2f}')

def compra_produtos(usuario, produtos):
    mostrar_produtos(produtos)
    opcoes = []
    for animal, dados in produtos['Carne'].items():
        opcoes.append(('Carne', animal, dados))
    for tipo in ['Ovos', 'Lã', 'Pele', 'Banha']:
        if produtos[tipo]:
            opcoes.append((tipo, None, produtos[tipo]))

    if len(opcoes) == 0:
        print('Nenhum produto disponível.')
        return

    for i, (tipo, subtipo, dados) in enumerate(opcoes):
        nome = f'{tipo} ({subtipo})' if subtipo else tipo
        print(f'({i+1}) {nome}')

    compra_produto = int(input('Qual produto deseja comprar? ')) - 1
    if compra_produto < 0 or compra_produto >= len(opcoes):
        print('Produto inválido.')
        return

    tipo, subtipo, dados = opcoes[compra_produto]
    quantia_produto = float(input('Quanto deseja comprar? '))
    if quantia_produto <= 0 or quantia_produto > dados['quantidade']:
        print('Quantia indisponível.')
        return

    preco_total = dados['preco'] * quantia_produto
    confirmacao = input(f'Total: R${preco_total:.2f}. Confirma? (s/n) ')
    if confirmacao != 's':
        print('Compra cancelada.')
        return

    dados['quantidade'] -= quantia_produto
    from dados import financeiro as fin
    fin['saldo'] += preco_total
    nome = f'{tipo} ({subtipo})' if subtipo else tipo
    print(f'Compra de {quantia_produto} {nome} realizada. Total: R${preco_total:.2f}')

def gerenciar_precos_leitederivados():
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