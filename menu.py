
user_adm = []
password_adm = []
user_c = []
password_c = []

index = -99
menu = -99
while menu != 0:
    menu = int(input('----MENU---- \n 1-Fazer login \n 2-Registrar \n 0-Fechar o programa \n'))
    if menu == 1:
        ml = int(input('1-Fazer login como ADM \n 2-fazer login como Cliente \n 0-Fechar o programa \n'))
        if ml == 1:
            id = input('Digite o nome de usuario: ')
            senha = input('Digite sua senha: ')
            if id in user_adm:
                i = user_adm.index(id)
                if senha == password_adm[i]:
                    print(f'Bem vindo ADM {id}')
                else:
                    print('senha invalida')
        elif ml == 2:
            id = input('Digite o nome de usuario: ')
            senha = input('Digite sua senha: ')
            if id in user_c:
                i = user_c.index(id)
                if senha == password_c[i]:
                    print(f'Bem vindo {id}')
                else:
                    print('senha invalida')
    if menu == 2:
        mr = int(input('1-Registrar como ADM \n 2-Registrar como Cliente \n 0-Fechar o programa \n'))
        if mr == 1:
            id = input('Digite o nome de usuario: ')
            senha = input('Digite sua senha: ')
            if id in user_adm:
                print('Usuario ja existente')
            else:
                user_adm.append(id)
                password_adm.append(senha)
        if mr == 2:
            id = input('Digite o nome de usuario: ')
            senha = input('Digite sua senha: ')
            if id in user_c:
                print('Usuario ja existente')
            else:
                user_c.append(id)
                password_c.append(senha)

print('programa finalizado')



