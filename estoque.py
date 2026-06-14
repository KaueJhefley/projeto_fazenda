from producao import leite_derivados,estoque_LeiteDerivados
from dados import produtos

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

def ver_estoque():
    print('\n======= ESTOQUE GERAL =======')
    print('\n--- LEITE E DERIVADOS ---')
    estoque_LeiteDerivados()
    
    print('\n--- PRODUTOS DO REBANHO ---')
    vazio = True
    for animal, dados in produtos['Carne'].items():
        vazio = False
        print(f'Carne ({animal}): {dados["quantidade"]} kg | R$ {dados["preco"]}')
    for tipo in ['Ovos', 'Lã', 'Pele', 'Banha']:
        if produtos[tipo]:
            vazio = False
            print(f'{tipo}: {produtos[tipo]["quantidade"]} | R$ {produtos[tipo]["preco"]}')
    if vazio:
        print('Nenhum produto do rebanho registrado.')