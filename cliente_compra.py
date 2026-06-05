def mostrar_leite_derivados(leite_derivados, preco_leite):

    print('\n----- ESTOQUE DISPONÍVEL -----\n')

    print(
        f'Leite disponível:\n'
        f'{leite_derivados["leite"]["disponivel"]} litros | '
        f'R$ {preco_leite}\n'
    )

    print('DERIVADOS DISPONÍVEIS:\n')

    if len(leite_derivados['derivados']) == 0:
        print('Nenhum derivado produzido ainda.')

    else:
        for item in leite_derivados['derivados']:

            unidade = 'L' if item[0] == 'Iogurte' else 'kg'

            print(f'{item[0]} {item[1]}: {item[2]} {unidade}')

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