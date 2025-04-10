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

# Caminho do arquivo CSV
local_arquivo = 'Formativa III/users.csv'

print("[ 1 ] Login\n[ 2 ] Cadastrar")
opcao = int(input('opcao: '))

if(opcao == 1) :
    login = input("Usuário: ")
    password = input("Senha: ")

    # Verifica se o usuário já existe no arquivo CSV
    usuario_encontrado = False
    usuarios = []

    # Lê o arquivo para verificar as credenciais e tentativas
    try:
        with open(local_arquivo, 'r', newline='') as arquivo:
            readerUsers = csv.reader(arquivo, delimiter=',')
            
            for loginConfirm, passwordConfirm, cont_tentativa_str in readerUsers:
                cont_tentativa = int(cont_tentativa_str)

                # Se o número de tentativas for 5 ou mais, bloqueia o usuário
                if cont_tentativa >= 5:
                    print(f"O usuário {loginConfirm} está bloqueado devido a muitas tentativas falhadas.")
                    usuario_encontrado = True
                    break

                # Se o login for encontrado, verifica se a senha está correta
                if login == loginConfirm:
                    usuario_encontrado = True
                    if password == passwordConfirm:
                        print(f"Seja bem-vindo(a), {loginConfirm}!")
                        break
                    else:
                        # Incrementa o contador de tentativas
                        cont_tentativa += 1
                        print("Login ou senha incorreto. Tente novamente.")

                        # Adiciona os dados modificados na lista de usuários
                        usuarios.append([loginConfirm, passwordConfirm, str(cont_tentativa)])
                        break

    except FileNotFoundError:
        print("Erro: O arquivo de usuários não foi encontrado.")

    # Se o login ou senha estiverem incorretos
    if not usuario_encontrado:
        print("Login ou senha incorreto. Tente novamente.")

    # Se o login foi encontrado e houve erro, ou se a senha estava incorreta, grava as alterações no arquivo
    if usuario_encontrado or not usuario_encontrado:
        try:
            with open(local_arquivo, 'w', newline='') as arquivo_escrita:
                writer = csv.writer(arquivo_escrita, delimiter=',', lineterminator='\n')
                writer.writerows(usuarios)
        except Exception as e:
            print(f"Erro ao atualizar o arquivo: {e}")

elif(opcao == 2):
    login = input("Usuário: ")
    password = input("Senha: ")
    with open(local_arquivo, 'a+', newline='') as arquivo:
        writer = csv.writer(arquivo, delimiter=',', lineterminator='\n')
        writer.writerow([login, password, 0])
else:
    print("Opção inválida!")