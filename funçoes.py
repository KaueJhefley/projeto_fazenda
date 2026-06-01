from dados import animais
def selecionar_tipo(tipo):
    tipos = {'1': 'bovino', '2': 'suino', '3': 'ave', '4': 'caprino', '5': 'ovino'}
    return tipos.get(tipo)
def selecionar_status(status_op):
    status = {'1': 'saudavel', '2': 'prenha ou choca', '3': 'doente'}
    return status.get(status_op)
def selecionar_lote(lote_op):
    lotes = {'1': 'venda', '2': 'abate', '3': 'leite e derivados', '4': 'reproducao', '5': 'tratamento'}
    return lotes.get(lote_op)
def validar_status_lote(status, lote):
    if status == 'prenha ou choca' and lote != 'reproducao':
        print('Erro: animais prenha ou choca só podem ir para o lote de reprodução')
        return False
    if status == 'doente' and lote != 'tratamento':
        print('Erro: animais doentes devem ir para o lote de tratamento')
        return False
    if status != 'doente' and lote == 'tratamento':
        print('Erro: apenas animais doentes devem ir para o lote de tratamento')
        return False
    return True