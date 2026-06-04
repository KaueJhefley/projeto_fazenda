maquinas = []

def registrar_maquina():
    print('----REGISTRAR MAQUINA----')
    tipo = input('Qual maquina será registrada? ')
    id = input('Qual o identificador da maquina? ')
    status = input('Qual o status da maquina?(funcionando/manutenção/defeito) ')
    maquinas.append({'tipo': tipo, 'identificador': id, 'status': status, 'motivo': ''})

def status_maquina():
    if len(maquinas) == 0:
        print("Nenhuma máquina cadastrada.")
        return
    print("----MÁQUINAS----")
    i = 0
    for m in maquinas:
        print(f"{i + 1} - {m['tipo']} | ID: {m['identificador']} | Status: {m['status']}")
        i += 1

    escolha = int(input("Qual máquina deseja alterar o status? "))
    if escolha < 1 or escolha > len(maquinas):
        print("Opção inválida.")
        return
    novo_status = input("Qual o novo status da máquina?((1)funcionando/(2)manutenção/(3)defeito) ")
    if novo_status == '1':
        maquinas[escolha - 1]['status'] = 'funcionando'
        print("Status atualizado com sucesso.")
        maquinas[escolha - 1]['motivo'] = ''
    elif novo_status == '2':
        maquinas[escolha - 1]['status'] = 'manutenção'
    elif novo_status == '3':
        maquinas[escolha - 1]['status'] = 'defeito'
        motivo = input("Qual o defeito da máquina? ")
        maquinas[escolha - 1]['motivo'] = motivo

def remover_maquina():
    if len(maquinas) == 0:
        print("Nenhuma máquina cadastrada.")
        return
    print("----MÁQUINAS----")
    i = 0
    for m in maquinas:
        print(f"{i + 1} - {m['tipo']} | ID: {m['identificador']} | Status: {m['status']}")
        i += 1 
    escolha = int(input("Qual máquina deseja remover?? "))
    if escolha < 1 or escolha > len(maquinas):
        print("Opção inválida.")
        return
    
    confirmacao = input('Deseja remover mesmo esta maquina? (s/n)')
    if confirmacao == 's':
        maquinas.pop(escolha - 1)
        print("Maquina removida com sucesso.")
    elif confirmacao == 'n':
        print('Ação cancelada.')
    else:
        return
    
def maquinas_indisponiveis():
    if len(maquinas) == 0:
        print("Nenhuma máquina cadastrada.")
        return
    print("---- MÁQUINAS INDISPONÍVEIS ----")
    encontrou = False
    for m in maquinas:
        if m['status'] in ['defeito', 'manutenção']:
            print(f"{m['tipo']} | ID: {m['identificador']} | Status: {m['status']} | Motivo: {m['motivo']}")
            encontrou = True
    if not encontrou:
        print("Nenhuma máquina indisponível no momento.")    
