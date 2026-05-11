agendamentos = []

while True:
    menu_agendamento = input('\n ----AGENDAR TRANSPORTE---- \n 1-Agendar retirada \n 2-Ver agendamentos \n 3-Cancelar agendamento \n 0-Retornar ao menu \n')

    if menu_agendamento == '1':
        dia_retirada = input('Informe o dia que sera feito a retirada: ')
        horario_retirada = input('Informe o horario da retirada: ')
        agendamentos.append([dia_retirada, horario_retirada])
        print('Agendamento feito com sucesso.')

    if menu_agendamento == '2':
        print('----AGENDAMENTOS EM ANDAMENTO----')
        for a in range(len(agendamentos)):
            print(f'dia: {agendamentos[a][0]} | horario: {agendamentos[a][1]}')

    if menu_agendamento == '3':
        print('----CANCELAR AGENDAMENTO----')
        if len(agendamentos) == 0:
            print('Nenhum agendamento em andamento.')
        else:    
            for a in range(len(agendamentos)):
                print(f'({a+1}) dia: {agendamentos[a][0]} | horario: {agendamentos[a][1]}')
            excluir_agendamento = int(input('Digite o agendamento que deseja cancelar: '))
            if excluir_agendamento < 1 or excluir_agendamento > len(agendamentos):
                print('Agendamento não encontrado.')
            else:
                agendamentos.pop(excluir_agendamento - 1)
                print('Agendamento cancelado com sucesso.')

    if menu_agendamento == '0':
        break 
