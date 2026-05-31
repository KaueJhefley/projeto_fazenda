import datetime

leite_derivados = {
    'leite': {
        'disponivel': 0,
        'historico': [],
    },
    'derivados': []
}

def producao_leite():
    dia_atual = datetime.date.today().strftime("%D/%m/%Y")
    leite_produzido = int(input('Quantos litros de leite foram produzidos? '))
    leite_derivados['leite']['disponivel'] += leite_produzido
    leite_derivados['leite']['historico'].append({'data': dia_atual, 'leite produzido':leite_produzido})

def registrar_derivado():
    if leite_derivados['derivados'] == []:
        print('Nenhum derivado disponível.')
        escolha_Nderivado = input('Deseja adicionar um novo derivado? (s/n) ')
        if escolha_Nderivado == 's':
            novo = input('Qual derivado deseja adicionar? ')
            leite_derivados['derivados'].append({'derivado': novo,'tipos': []})
            print('Derivado adicionado com sucesso.')
        return
    print('\n ----DERIVADOS DISPONIVEIS---- \n')
    i = 0
    for d in leite_derivados['derivados']:
        print(f'({i+1}) - {d["derivado"]}')
        i += 1
    escolha = int(input('Qual derivado deseja registrar? ')) - 1
    if escolha < 0 or escolha >= len(leite_derivados['derivados']):
        print('Opção inválida.')
        return
    derivado_escolhido = leite_derivados['derivados'][escolha]

    tipo = input(f"Qual tipo de {derivado_escolhido['derivado']} deseja adicionar? ")
    for t in derivado_escolhido['tipos']:
        if t['tipo'] == tipo:
            print('Esse tipo já existe para esse derivado.')
            return
    derivado_escolhido['tipos'].append({'tipo': tipo})
    print('Tipo de derivado registrado com sucesso.')

def produzir_derivado():
    print('------PRODUÇÃO DE DERIVADOS------')
    print(f"LEITE DISPONIVEL: {leite_derivados['leite']['disponivel']} LITROS")

    if leite_derivados['derivados'] == []:
        print('Nenhum derivado disponivel.')
    else:
        print('\n ----DERIVADOS DISPONIVEIS---- \n')
        i = 0
        for d in leite_derivados['derivados']:
            print(f'({i+1}) - {d["derivado"]}')
            i += 1
        escolha = int(input('Qual derivado deseja produzir? ')) - 1
        if escolha < 0 or escolha >= len(leite_derivados['derivados']):
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
        escolha_tipo = int(input('Qual tipo deseja produzir? ')) - 1
        if escolha_tipo < 0 or escolha_tipo >= len(derivado_escolhido['tipos']):
            print('Tipo inválido.')
            return
        tipo = derivado_escolhido['tipos'][escolha_tipo]
        quantidade = float(input('Quantos Kg/L foram produzidos? '))
        leite_gasto = float(input('Quantos litros de leite foram usados? '))
        if leite_gasto > leite_derivados['leite']['disponivel']:
            print('Leite insuficiente.')
            return
        leite_derivados['leite']['disponivel'] -= leite_gasto
        if 'estoque' not in tipo:
            tipo['estoque'] = 0
        tipo['estoque'] += quantidade
        print('\nProdução registrada com sucesso.')

def estoque_LeiteDerivados():
    print(f"LEITE DISPONÍVEL: {leite_derivados['leite']['disponivel']} L\n")

    if leite_derivados['derivados'] == []:
        print("Nenhum derivado cadastrado.")
        return
    for derivado in leite_derivados['derivados']:
        print(derivado['derivado'])
        if derivado['tipos'] == []:
            print("  - Nenhum tipo cadastrado")
        else:
            for tipo in derivado['tipos']:
                if 'estoque' in tipo:
                    estoque = tipo['estoque']
                else:
                    estoque = 0
                print(f"  - {tipo['tipo']} | Estoque: {estoque}")