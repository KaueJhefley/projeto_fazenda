from producao_leite_derivados import leite_derivados
from producao_leite_derivados import estoque_LeiteDerivados

def atualizar_preco():
    print(estoque_LeiteDerivados())
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

def atualizar_quantia_estoque():
    