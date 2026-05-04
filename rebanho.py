#gerenciar rebanho
bovinos = []
suinos = []
aves = []
index = -99
op = -99
#opções 
while op != '0':
    op = input('------O que deseja fazer?------ \n 1-Cadastrar Animal \n 2-Buscar Animal \n 3-Atualizar Rebanho \n 4-Remover \n 5-gerenciamento de lotes \n 0-retornar ao menu \n')
    if op == '1':
        tipo = input('----Que tipo de animal deseja registrar---- \n 1-bovino \n 2-suino \n 3-ave \n')
        

        identificacao = input('Digite a identificação do animal: ')
        status = input('Qual o status do animal\n1-saudavel\n2-prenha ou choca\n3-doente\n')
        if status == '1':
            status = 'saudavel'
        elif status == '2':
            status = 'prenha ou choca'
        elif status == '3':
            status = 'doente'
        lote_op = input('Para qual lote o animal deve ir?\n1-Lote para venda \n2-lote para abate \n3-lote para producao de leite e derivados \n4-reproduçao\n5-tratamento\n')
        if lote_op == '1':
            lote = 'venda'
        elif lote_op == '2':
            lote = 'abate'
        elif lote_op == '3':
            lote = 'producao'
        elif lote_op == '4':
            lote = 'reproducao'
        elif lote_op == '5':
            lote = 'tratamento'
        if status == 'prenha ou choca' and lote != 'reproducao':
            print('Erro: animais prenha ou choca só podem ir para o lote de reprodução')
            continue
        if status == 'doente' and lote != 'tratamento':
            print('Erro: animais doentes devem ir para o lote de tratamento')
            continue
        if status != 'doente' and lote == 'tratamento':
            print('Erro: apenas animais doentes devem ir para o lote de tratamento')
            continue
        animal = [identificacao, status,lote]

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
        if not encontrado:
            print('Animal não encontrado')

    elif op == '4':
        remover = input('----Que tipo de animal deseja remover---- \n 1-bovino \n 2-suino \n 3-ave \n')
        busca = input('Digite a identificação do animal: ')
        if remover == '1':
                lista = bovinos
        elif remover == '2':
            lista = suinos
        elif remover == '3':
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
    elif op == '5':
        gl = input('1 - Ver animais por lote\n2 - Mover animal de lote\n')
        if gl == '1':
            lote_busca = input('1-Lote para venda \n 2-lote para abate \n 3-lote para produçao de leite e derivados \n 4-lote para reproduçao \n 5-lote para tratamento\n')
            if lote_busca == '1':
                nome_lote = 'venda'
            elif lote_busca == '2':
                nome_lote = 'abate'
            elif lote_busca == '3':
                nome_lote = 'producao'
            elif lote_busca == '4':
                nome_lote = 'reproducao'
            elif lote_busca == '5':
                nome_lote = 'tratamento'

            else:
                print('Lote inválido')
                continue
            print('----BOVINOS----')
            for a in bovinos:
                if a[2] == nome_lote:
                    print(a)

            print('---- SUINOS ----')
            for a in suinos:
                if a[2] == nome_lote:
                    print(a)

            print('---- AVES ----')
            for a in aves:
                if a[2] == nome_lote:
                    print(a)