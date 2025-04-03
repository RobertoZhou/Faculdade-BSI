# ETAPA 1
# Desenvolva um programa, na linguagem Python ou Java, que realize a autenticação do usuário. O programa deve armazenar o nome de usuário e sua senha.

# O usuário deve entrar com o login e a senha no programa seguindo casos:

# Se o login E a senha estiverem corretas, mostre “Seja bem vindo, {login}” (substitua {login} pelo nome de usuário)
# Se o login OU a senha estiverem incorretas, mostre “Login ou senha incorreto. Tente novamente mais tarde.”
# Considere armazenar a senha em um arquivo no seu sistema (CSV ou JSON).

 

# ETAPA 2
# Com base na etapa anterior, implemente o seguinte mecanismo:

# Caso o usuário erre a senha MAIS DE 5 VEZES, bloqueie o seu acesso ao sistema.
# Sugestão: Criar arquivo no seu sistema para armazenar os usuários bloqueados

import csv

login = input("Usuário: ")
password = input("Senha: ")

cont_tentativa = 0

local_arquivo = 'Segurança da Informação/Formativa III/users.csv'

with open(local_arquivo, "a+", newline='') as arquivo:
    writeUser = csv.writer(arquivo, delimiter=',', lineterminator='\n')   
    writeUser.writerow([login, password, cont_tentativa]) 


for i in range(6):
    login = input("Usuário: ")
    password = input("Senha: ")
    with open(local_arquivo, "r") as arquivo:
        readerUsers = csv.reader(arquivo, delimiter=',')

        for loginConfirm, passwordConfirm, cont_tentativa in readerUsers:
            if(cont_tentativa == 5):
                print('ERRO')
                break
            else:
                if(login == loginConfirm):
                    if(password == passwordConfirm):
                        print(f'Seja bem-vindo(a), {loginConfirm}!')
                        break
                    else:
                        with open(local_arquivo, 'r') as arquivo:
                            linhas = csv.reader(arquivo, delimiter=',')
                            LINHAS = [linha for linha in linhas]
                            
                        with open(local_arquivo, "w", newline='') as arquivo:
                            writer = csv.writer(arquivo)
                            for linha in LINHAS:
                                if linha[0] == login:
                                    writer.writerow([linha[0], linha[1], cont_tentativa])
                            print('Login ou senha incorreto! Tente novamente mais tarde.')
            break