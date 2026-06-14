import matplotlib
import matplotlib.pyplot as plt

def grafico_producao_leite(leite_derivados):
    historico = leite_derivados['leite']['historico']
    if not historico:
        print("Nenhum dado de produção registrado.")
        return
    datas = []
    producao = []
    for registro in historico:
        datas.append(registro['data'])
        producao.append(registro['leite produzido'])
    plt.figure(figsize=(10, 5))
    plt.plot(datas, producao, marker='o')

    plt.title("Produção de Leite")
    plt.xlabel("Data")
    plt.ylabel("Litros Produzidos")
    plt.grid(True)

    plt.tight_layout()
    plt.show()

def grafico_vendas_leite_derivados(historico_vendas):
    produtos = {}
    faturamento = {}
    if not historico_vendas:
        print("Nenhuma venda registrada.")
        return
    
    else:
        for venda in historico_vendas:
            produto = venda['produto']
            if produto not in produtos:
                produtos[produto] = 0
                faturamento[produto] = 0
            produtos[produto] += venda['quantidade']
            faturamento[produto] += venda['valor']
        nomes = list(produtos.keys())
        quantidades = list(produtos.values())
        valores = list(faturamento.values())
        fig, ax1 = plt.subplots(figsize=(10, 5))

        ax1.bar(nomes, quantidades, label="Quantidade Vendida")
        ax1.set_ylabel("Quantidade Vendida")
        ax1.grid(True, axis='y')
        ax1.legend(loc='upper left')

        ax2 = ax1.twinx()
        ax2.plot(nomes, valores, marker='o', label="Faturamento (R$)")
        ax2.set_ylabel("Faturamento (R$)")
        ax2.legend(loc='upper right')

        plt.title("Vendas e Faturamento por Produto")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

def grafico_faturamento_dia(historico_vendas):
    if not historico_vendas:
        print("Nenhuma venda registrada.")
        return
    faturamento = {}
    for venda in historico_vendas:
        data = venda['data']
        if data not in faturamento:
            faturamento[data] = 0
        faturamento[data] += venda['valor']
    datas = list(faturamento.keys())
    valores = list(faturamento.values())

    plt.figure(figsize=(10, 5))
    plt.plot(datas, valores, marker='o')
    plt.title("Faturamento por Dia")
    plt.xlabel("Data")
    plt.ylabel("Faturamento (R$)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()