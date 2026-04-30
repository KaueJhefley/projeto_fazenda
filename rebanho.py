#gerenciar rebanho
animais = []
bovinos = []
suinos = []
aves = []
index = -99
op = -99
#opções 
while op != '0':
    op = input('------O que deseja fazer?------ \n 1-Cadastrar Animal \n 2-Buscar Animal \n 3-Atualizar Rebanho \n 4-Remover Animal \n 0-retornar ao menu \n')
    if op == '1':
        tipo = input('----Que tipo de animal deseja registrar---- \n 1-bovino \n 2-suino \n 3-ave \n')
        

        identificacao = input('Digite a identificação do animal: ')
        status = input('Digite o Status do animal: ')
        animal = [identificacao, status]

        if tipo == '1':
            lista = bovinos
        elif tipo == '2':
            lista = suinos
        elif tipo == '3':
            lista = aves
        else:
            print('Tipo inválido')
            continue

        existe = False
        for a in lista:
            if a[0] == identificacao:
                existe = True
                break

        if existe:
            print('Animal já existente')
        else:
            lista.append(animal)
            print('Animal cadastrado')

    elif op == '2':
        tipo = input('----Que tipo de animal deseja encontrar---- \n'
                     '1-bovino \n'
                     '2-suino \n'
                     '3-ave \n')

        busca = input('Digite a identificação do animal: ')

        if tipo == '1':
                lista = bovinos
        elif tipo == '2':
            lista = suinos
        elif tipo == '3':
            lista = aves
        else:
            print('Tipo inválido')
            continue

        encontrado = False
        for a in lista:
            if a[0] == busca:
                print('Animal encontrado:', a)
                encontrado = True
                break

        if not encontrado:
            print('Animal não encontrado')
    elif op == '3':
        atualizar = input('----Que tipo de animal deseja atualizar---- \n 1-bovino \n 2-suino \n 3-ave \n')
        busca = input('Digite a identificação do animal: ')
        if atualizar == '1':
                lista = bovinos
        elif atualizar == '2':
            lista = suinos
        elif atualizar == '3':
            lista = aves
        else:
            print('Tipo inválido')
            continue
        
        encontrado = False
        for animal in lista:
            if animal[0] == busca:
                print('Animal encontrado:', animal)
                novo_status = input('Digite o novo status: ')
                animal[1] = novo_status
                print('Animal atualizado')
                encontrado = True
                break
            else:
                print('animal nao encontrado')

    elif op == '4':
        atualizar = input('----Que tipo de animal deseja remover---- \n 1-bovino \n 2-suino \n 3-ave \n')
        busca = input('Digite a identificação do animal: ')
        if atualizar == '1':
                lista = bovinos
        elif atualizar == '2':
            lista = suinos
        elif atualizar == '3':
            lista = aves
        else:
            print('Tipo inválido')
            continue
        encontrado = False
        for animal in lista:
            if animal[0] == busca:
                print('Animal encontrado:', animal)
                pergunta = input('Tem certeza que deseja remover esse animal? \n 1-sim \n 2-nao \n')
                if pergunta == '1':
                    lista.remove(animal)
                    encontrado = True
                    print('Animal removido')
                    break
        if not encontrado:
            print('Animal não encontrado')

    



