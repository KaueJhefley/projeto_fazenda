from funçoes import selecionar_lote,selecionar_status,selecionar_tipo,validar_status_lote
from dados import animais
def cadastrar_animal():
    tipo = input('----Que tipo de animal deseja registrar---- \n 1-bovino \n 2-suino \n 3-ave \n 4-caprino\n5-ovino\n')
    tipo = selecionar_tipo(tipo)
    if tipo is None:
        print('Tipo invalido')
        return None
    identificacao = input('Digite a identificação do animal: ')
    if identificacao in animais[tipo]:
        print('Animal já existente')
        return
    status = input('Qual o status do animal\n1-saudavel\n2-prenha ou choca\n3-doente\n')
    status = selecionar_status(status)
    if status is None:
        print('status invalido')
        return 

    lote_op = input('Para qual lote o animal deve ir?\n1-Lote para venda \n2-lote para abate \n3-lote para producao de leite e derivados \n4-reproduçao\n5-tratamento\n')
    lote = selecionar_lote(lote_op)
    if lote is None:
        print('Lote invalido')
        return
    
    if not validar_status_lote(status, lote):
        return
    animais[tipo][identificacao] = {'status': status, 'lote': lote}
    print('Animal cadastrado:', identificacao, '->', animais[tipo][identificacao])

def buscar_animal():
    tipo = input('----Que tipo de animal deseja encontrar----\n1-bovino\n2-suino\n3-ave\n4-caprino\n5-ovino\n')
    tipo = selecionar_tipo(tipo)
    if tipo is None:
        print('Tipo invalido')
        return
    identificaçao = input('Digite a identificaçao do animal: ')
    if identificaçao in animais[tipo]:
        print('Animal encontrado:', identificaçao, '->', animais[tipo][identificaçao])
    else:
        print('Animal nao encontrado')
def atualizar_animal():
    tipo = input('----Que tipo de animal deseja atualizar----\n1-bovino\n2-suino\n3-ave\n4-caprino\n5-ovino\n')
    tipo = selecionar_tipo(tipo)
    if tipo is None:
        print('Tipo inválido')
        return
    identificacao = input('Digite a identificação do animal: ')
    if identificacao not in animais[tipo]:
        print('Animal não encontrado')
        return
    print('Animal encontrado:', identificacao, '->', animais[tipo][identificacao])
    status_op = input('Qual o novo status\n1-saudavel\n2-prenha ou choca\n3-doente\n')
    status = selecionar_status(status_op)
    if status is None:
        print('Status inválido')
        return
    lote_op = input('Para qual lote?\n1-venda\n2-abate\n3-leite e derivados\n4-reprodução\n5-tratamento\n')
    lote = selecionar_lote(lote_op)
    if lote is None:
        print('Lote inválido')
        return

    if not validar_status_lote(status, lote):
        return

    animais[tipo][identificacao] = {'status': status, 'lote': lote}
    print('Animal atualizado:', identificacao, '->', animais[tipo][identificacao])

def remover_animal():
    tipo = input('----Que tipo de animal deseja remover----\n1-bovino\n2-suino\n3-ave\n4-caprino\n5-ovino\n')
    tipo = selecionar_tipo(tipo)
    if tipo is None:
        print('Tipo inválido')
        return

    identificacao = input('Digite a identificação do animal: ')
    if identificacao not in animais[tipo]:
        print('Animal não encontrado')
        return
    print('Animal encontrado:', identificacao, '->', animais[tipo][identificacao])
    confirmacao = input('Tem certeza?\n1-sim\n2-nao\n')
    if confirmacao == '1':
        del animais[tipo][identificacao]
        print('Animal removido')
def gerenciar_lotes():
    lote_op = input('1-venda\n2-abate\n3-leite e derivados\n4-reprodução\n5-tratamento\n')
    lote = selecionar_lote(lote_op)
    if lote is None:
        print('Lote inválido')
        return
    for tipo, rebanho in animais.items():
        print(f'---- {tipo} ----')
        animais_no_lote = {}
        for identificacao, dados in rebanho.items():
            if dados['lote'] == lote:
                animais_no_lote[identificacao] = dados
        if animais_no_lote:
            for identificacao, dados in animais_no_lote.items():
                print(f'  {identificacao}: {dados}')
        else:
            print('Nenhum animal neste lote')




