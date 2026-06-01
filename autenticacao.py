from dados import admins, clientes
def login_adm():
    usuario = input('Digite o nome de usuario: ')
    senha = input('Digite sua senha: ')
    if usuario in admins:
        if senha == admins[usuario]:
            print(f'Bem vindo, ADM {usuario}')
            return usuario
        else:
            print('senha invalida')
            return None
    else:
        print('usuario nao existente')
        return None
            
    
def login_cliente():
    usuario = input('Digite o nome de usuario: ')
    senha = input('Digite sua senha: ')
    if usuario in clientes:
        if senha == clientes[usuario]:
            print(f'Bem vindo, {usuario}')
            return usuario
        else:
            print('Senha invalida')
            return None
    else:
        print('Usuario nao encontrado')
        return None
def registrar_adm():
    usuario = input('Digite o nome de usuario: ')
    senha = input('Digite sua senha: ')
    if usuario in admins:
        print('usuario ja existente')
    else:
        admins[usuario] = senha

    

def registrar_cliente():
    usuario = input('Digite o nome de usuario: ')
    senha = input('Digite sua senha: ')
    if usuario in clientes:
        print('usuario ja existente')
    else:
        clientes[usuario] = senha