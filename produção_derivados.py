#Cadastrar a produção diária
producao_leite = []

#cadastrar produtos
produtos = []

while True:

    op = input('------O que deseja fazer?------ \n 1-Registrar produção de leite \n 2-Atualizar alimentos \n 0-retornar ao menu \n')

    if op == '1':
        dia = input('Digite o dia atual: ')
        litros = float(input('Digite a quantia ordenhada: '))

        atualizar_valor = [dia, litros]
        producao_leite.append(atualizar_valor)

        print('Produção cadastrada.')
    
    elif op == '2':
        while True:
            att_alimentos = input('--------O que deseja atualizar?------ \n 1-Registrar Alimento \n 2-remover produto \n 3-Atualizar preços \n 0-Cancelar')
            
            if att_alimentos == '1':
                produto = input('Qual produto deseja adicionar?')
                peso = float(input('Qual o peso do produto?'))
                preço = float(input('Qual o preço do produto?'))

                alimento = [produto, peso, preço]
                produtos.append(alimento)

                print('Produtos atualizados.')

            elif att_alimentos == '2':
                busca = input('Digite o produto que deseja eliminar: ')
                index = -1

                for i in range(len(produtos)):
                    if busca == produtos[i][0]:
                        index = i
                        break

                if index >= 0:
                    produtos.pop(index)
                    print('Produto removido.')
                else:
                    print('Não foi possível eliminar este produto.')
            
            elif att_alimentos == '3':
                busca = input('Digite o alimento que deseja atualizar o preço: ')
                encontrado = 0
                for alimento in produtos:
                    if alimento[0] == busca: 
                        print('Alimento encontrado: ', alimento)
                        novo_status = input('Digite o novo preço: ')
                        alimento[2] = novo_status 
                        print('Alimento Atualizado.')
                        encontrado = 1
                    
                    if encontrado == 0:
                        print('Alimento não encontrado.')

            elif att_alimentos == '0':
                break
    
    elif op == '0':
        break


