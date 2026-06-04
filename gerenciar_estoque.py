from producao_leite_derivados import leite_derivados
from producao_leite_derivados import estoque_LeiteDerivados

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
