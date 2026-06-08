from producao_leite_derivados import leite_derivados
import datetime
historico_vendas = []

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

def compra_leite_derivados():
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
                    leite_derivados['leite']['disponivel'] -= quantia_leite
                    valor_total = quantia_leite * leite_derivados['leite']['preco']
                    print(f'O valor total foi de: R${valor_total}')
                    confirmacao = input('deseja realizar a compra? (s/n)')
                    if confirmacao == 's':
                       valor_total = quantia_leite * leite_derivados['leite']['preco']
                       historico_vendas.append({
                       'data': datetime.date.today().strftime("%d/%m/%Y"),
                       'produto': 'Leite',
                       'quantidade': quantia_leite,
                       'valor': valor_total
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
                if escolha < 0 or escolha > len(leite_derivados['derivados']):
                    print('Opção inválida.')
                    return
                derivado_escolhido = leite_derivados['derivados'][escolha]
                if derivado_escolhido['tipos'] == []:
                    print('Esse derivado não possui tipos cadastrados.')
                    return
            i = 0
            for t in derivado_escolhido['tipos']:
                print(f'({i+1}) {t["tipo"]}')
                i += 1
            escolha_tipo = int(input('Qual tipo deseja escolher?(numero) ')) - 1
            if escolha_tipo < 0 or escolha_tipo >= len(derivado_escolhido['tipos']):
                print('Tipo inválido.')
                return
            tipo = derivado_escolhido['tipos'][escolha_tipo]
            quantidade = float(input('Quantos Kg/L deseja comprar? '))
            if quantidade <= 0 or quantidade > tipo['estoque']:
                print('Quantia indisponivel.')
            else:
                valor_total = quantidade * tipo['preco']
                print(f'O total da compra sera: R${valor_total}')
                confirmacao = input('Deseja finalizar a compra? (s/n)')
                if confirmacao == 's':
                    valor_total = quantia_leite * leite_derivados['leite']['preco']
                    tipo['estoque'] -= quantidade
                    historico_vendas.append({
                    'data': datetime.date.today().strftime("%d/%m/%Y"),
                    'produto': f"{derivado_escolhido['derivado']} - {tipo['tipo']}",
                    'quantidade': quantidade,
                    'valor': valor_total
                    })    
                    print('Compra realizada com sucesso.')
                elif confirmacao == 'n':
                    print('Compra cancelada') 
                else:
                    print('Escolha invalida.')
                    return

