receitas = []
despesas = []
saldo = 0


while True:
    financeiro = input('----Gerenciamento Financeiro---- \n 1-registrar receita \n 2-registrar despesa \n 3-ver saldo\n 4-relatorio financeiro\n 0-voltar\n')
    if financeiro == '1':
        descricao = input('Digite a descrição da receita: ')
        valor = float(input('Digite o valor da receita: '))
        data = input('Digite a data da receita (DD/MM/AAAA): ')
        receitas.append([descricao, valor, data])
        saldo += valor
        print('Receita registrada com sucesso.')
    elif financeiro == '2':
        descricao = input('Digite a descrição da despesa: ')
        valor = float(input('Digite o valor da despesa: '))
        data = input('Digite a data da despesa (DD/MM/AAAA): ')
        despesas.append([descricao, valor, data])
        saldo -= valor
        print('Despesa registrada com sucesso.')
    elif financeiro == '3':
        print('saldo atual: R$', saldo)
    elif financeiro == '4':
        print('----RELATÓRIO FINANCEIRO----')
        print('----Receitas----')
        for r in receitas:
            print(f'{r[0]} - R$ {r[1]} - {r[2]}')
        print('----Despesas----')
        for d in despesas:
            print(f'{d[0]} - R$ {d[1]} - {d[2]}')
    elif financeiro == '0':
        break
