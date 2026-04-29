#gerenciar rebanho
animais = []

#opções 
op = input('------O que deseja fazer?------ \n 1-Cadastrar Animal \n 2-Buscar Animal \n 3-Atualizar Rebanho \n 4-Remover Animal \n 0-retornar ao menu \n')

if op == '1':
    tipo = input('Digite o tipo do animal: ')
    identificacao = input('Digite a identificação do animal: ')
    status = input('Digite o Status do animal: ')

    animal = [tipo, identificacao, status]
    animais.append(animal)
    
    print('Animal Cadastrado.')

elif op == '2':
    busca = input('Digite o animal que deseja encontrar: ')
    for i in range(len(animais)):
        index = 1
        print(index)
        break

elif op == '3':
    busca = input('Digite a identificação que deseja atualizar:')
    
    for animal in animais:
        if animal == busca:
            print('Animal encontrado: ', animal)

            novo_status = input('Digite o novo status: ')
            animais[2] = novo_status

            print('Animal Atualizado.')
        
        else:
            print('Animal não encontrado: ')

elif op == '4':
    busca = input('Digite o animal que deseja eliminar: ')
    for i in range(len(animais)):
        if busca == animais[i]:
            index = i
            print(index)
            break
    if index >= 0:
        animais.pop(index)
        print('Animal Removido.')
    
    else:
        print('Não foi possivel eliminar este animal.')

elif op == '0':
    




