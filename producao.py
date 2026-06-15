import datetime
from dados import leite_derivados

def producao_leite():
    dia_atual = datetime.date.today().strftime("%d/%m/%Y")
    leite_produzido = int(input('Quantos litros de leite foram produzidos?(numero) '))
    leite_derivados['leite']['disponivel'] += leite_produzido
    leite_derivados['leite']['historico'].append({'data': dia_atual, 'leite produzido':leite_produzido})

def cadastrar_derivado():
    novo_derivado = input('Nome do novo derivado: ')
    for derivado in leite_derivados['derivados']:
        if derivado['derivado'].lower() == novo_derivado.lower():
            print('Esse derivado já existe.')
            return
    leite_derivados['derivados'].append({'derivado': novo_derivado,'tipos': []})
    print('Derivado cadastrado com sucesso.')

def cadastrar_tipo_derivado():
    if leite_derivados['derivados'] == []:
        print('Nenhum derivado cadastrado.')
        return
    print('\n---- DERIVADOS DISPONÍVEIS ----\n')
    i = 0
    for derivado in leite_derivados['derivados']:
        print(f'({i+1}) - {derivado["derivado"]}')
        i += 1

    escolha = int(input('Escolha o derivado: ')) - 1
    if escolha < 0 or escolha >= len(leite_derivados['derivados']):
        print('Opção inválida.')
        return
    derivado_escolhido = leite_derivados['derivados'][escolha]
    tipo = input(f'Qual tipo deseja adicionar em \n {derivado_escolhido["derivado"]}? ')
    for t in derivado_escolhido['tipos']:
        if t['tipo'].lower() == tipo.lower():
            print('Esse tipo já existe.')
            return
    derivado_escolhido['tipos'].append({'tipo': tipo,'estoque': 0,'preco': 0,'historico': []})
    print('Tipo cadastrado com sucesso.')

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
        escolha = int(input('Qual derivado deseja produzir?(numeros): ')) - 1
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
        dia_atual = datetime.date.today().strftime("%d/%m/%Y")
        tipo['historico'].append({'data': dia_atual,'produzido': quantidade,'estoque': tipo['estoque'],'leite_gasto': leite_gasto})
        print('\nProdução registrada com sucesso.')

def estoque_LeiteDerivados():
    print(f"LEITE DISPONÍVEL: {leite_derivados['leite']['disponivel']} Litros\nPreço: R${leite_derivados['leite']['preco']}")

    i = 0
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
                print(f" {i+1} - {tipo['tipo']} | Estoque: {estoque}| Preço: R${tipo['preco']}")
                i += 1
