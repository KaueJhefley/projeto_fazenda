from producao import leite_derivados,estoque_LeiteDerivados
from dados import produtos


def atualizar_preco():
    if len(leite_derivados['derivados']) == 0:
        print("Nenhum produto cadastrado.")
        return
    escolha_produto = input('Qual produto deseja alterar o preço? \n 1-Leite \n 2-Derivados \n 0-Cancelar')

    if escolha_produto == '1':
        print(f"Preço atual do leite: {leite_derivados['leite']['preco']}")
        novo_preco = float(input('Qual será o novo preço do leite?(L) '))
        if novo_preco <= 0:
            print('Ação Cancelada/Valor invalido.')
        else:
            leite_derivados['leite']['preco'] = novo_preco

    elif escolha_produto == '2':
        estoque_LeiteDerivados()
        opcoes = []
        for derivado in leite_derivados['derivados']:
            for tipo in derivado['tipos']:
                opcoes.append(tipo)
        if len(opcoes) == 0:
            print('Nenhum produto disponível.')
            return

        escolha = int(input('\nQual produto deseja alterar o preço? '))
        if escolha < 0 or escolha >= len(opcoes):
            print('Opção inválida.')
            return
        novo_preco = float(input('Digite o preço: R$ '))
        opcoes[escolha]['preco'] = novo_preco
        print('Preço atualizado com sucesso!')
    elif escolha_produto == '0':
        print('Ação cancelada.')

def registrar_produto(produtos):

    registro_produto = input(
        '\n----Qual produto deseja registrar?----\n'
        '(1)Carne\n'
        '(2)Ovos\n'
        '(3)Lã\n'
        '(4)Pele\n'
        '(5)Banha\n'
        '(0)Cancelar\n'
    )

    if registro_produto == '0':
        return

    elif registro_produto == '1':

        carne_escolha = input(
            '\n----CARNES----\n'
            '(1)Bovina\n'
            '(2)Suínos\n'
            '(3)Aves\n'
            '(4)Caprino\n'
            '(5)Ovino\n'
            '(0)Cancelar\n'
        )

        if carne_escolha == '0':
            return
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
            return

        quantidade = float(input('Digite a quantidade disponível: '))
        preco = float(input('Digite o preço do produto: '))

        if animal in produtos["Carne"]:
            produtos["Carne"][animal]["quantidade"] += quantidade
            produtos["Carne"][animal]["preco"] = preco

            print(
                f'Produto atualizado. Nova quantidade: '
                f'{produtos["Carne"][animal]["quantidade"]}'
            )

        else:
            produtos["Carne"][animal] = {
                "quantidade": quantidade,
                "preco": preco
            }

            print(
                f'{quantidade} de Carne ({animal}) '
                f'adicionados ao estoque.'
            )

    elif registro_produto == '2':
        tipo_produto = 'Ovos'

    elif registro_produto == '3':
        tipo_produto = 'Lã'

    elif registro_produto == '4':
        tipo_produto = 'Pele'

    elif registro_produto == '5':
        tipo_produto = 'Banha'

    else:
        print('Opção inválida.')
        return

    # Produtos que não são carne
    if registro_produto in ['2', '3', '4', '5']:

        quantidade = float(input('Digite a quantidade disponível: '))
        preco = float(input('Digite o preço do produto: '))

        if produtos[tipo_produto]:

            produtos[tipo_produto]["quantidade"] += quantidade
            produtos[tipo_produto]["preco"] = preco

            print(
                f'Produto atualizado. Nova quantidade: '
                f'{produtos[tipo_produto]["quantidade"]}'
            )

        else:

            produtos[tipo_produto] = {
                "quantidade": quantidade,
                "preco": preco
            }

            print(
                f'{quantidade} de {tipo_produto} '
                f'adicionados ao estoque.'
            )

def ver_estoque(leite_derivados, produtos):

    print('\n--- Estoque de Leite ---')
    print(leite_derivados['leite']['disponivel'], 'litros')

    print('\n--- Derivados ---')

    if len(leite_derivados['derivados']) == 0:
        print('Nenhum derivado produzido.')

    else:
        for item in leite_derivados['derivados']:

            if item[0] == 'Iogurte':
                unidade = 'L'
            else:
                unidade = 'kg'

            print(f"{item[0]} {item[1]}: {item[2]} {unidade}")

    print('\n--- Produtos do Rebanho ---')

    vazio = True

    # Carnes
    for animal, dados in produtos['Carne'].items():

        vazio = False

        print(
            f"Carne ({animal}): "
            f"{dados['quantidade']} "
            f"- R${dados['preco']}"
        )

    # Ovos, Lã, Pele e Banha
    for tipo in ['Ovos', 'Lã', 'Pele', 'Banha']:

        if produtos[tipo]:

            vazio = False

            print(
                f"{tipo}: "
                f"{produtos[tipo]['quantidade']} "
                f"- R${produtos[tipo]['preco']}"
            )

    if vazio:
        print('Nenhum produto registrado.')



