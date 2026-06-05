from dados import financeiro
saldo = 0

def registrar_receita():
    descricao = input('Digite a descrição da receita: ')
    valor = float(input('Digite o valor da receita: '))
    data = input('Digite a data da receita (DD/MM/AAAA): ')
    id_receita = len(financeiro['receitas']) + 1
    financeiro['receitas'][id_receita] = {
        'descricao': descricao,
        'valor': valor,
        'data': data
    }
    financeiro['saldo'] += valor
    print('Receita registrada com sucesso.')

def registrar_despesas():
    descricao = input('Digite a descrição da despesa: ')
    valor = float(input('Digite o valor da despesa: '))
    data = input('Digite a data da despesa (DD/MM/AAAA): ')
    id_despesa = len(financeiro["despesas"]) + 1
    financeiro["despesas"][id_despesa] = {
        "descricao": descricao,
        "valor": valor,
        "data": data
    }
    financeiro['saldo'] -= valor
    print('Despesa registrada com sucesso')
def relatorio_financeiro():
    print('---- RECEITAS ----')
    for id_receita, receita in financeiro["receitas"].items():
        print(
            f'{id_receita} - '
            f'{receita["descricao"]} - '
            f'R$ {receita["valor"]} - '
            f'{receita["data"]}'
        )
    print('---- DESPESAS ----')
    for id_despesa, despesa in financeiro["despesas"].items():
        print(
            f'{id_despesa} - '
            f'{despesa["descricao"]} - '
            f'R$ {despesa["valor"]} - '
            f'{despesa["data"]}'
        )
def ver_saldo():
    print('saldo atual: R$', financeiro['saldo'])
