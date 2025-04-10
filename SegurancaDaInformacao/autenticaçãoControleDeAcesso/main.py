#   Requisitos:​
# 1. O usuário deve entrar com o seu login e senha​ (autenticação) e ter a funcionalidade de cadastrar usuário
#   1.1 Se o usuário estiver autenticado, continue a execução do programa
#   1.2 Caso contrário, saia do programa e mostre a mensagem "Usuário ou senha inválidos" na tela
#   1.3 Um novo usuário cadastrado não deverá ter permissão para nenhum arquivo
# 2. A relação usuário/senha deve estar armazenado em um arquivo (TXT, CSV ou JSON)
# 3. As permissões dos usuários devem estar armazenadas em um arquivo (TXT, CSV ou JSON)
# 4. O sistema deve perguntar ao usuário qual ação ele deseja realizar (ler, escrever ou apagar) sobre um recurso fictício
#  4.1 No contexto do trabalho, o recurso fictício, no caso, não é um arquivo existente no sistema
# 5. Ele deverá especificar a ação que deseja realizar (ler, escrever, apagar) sobre um recurso
# 6. O sistema deve perguntar ao usuário qual arquivo ele deseja realizar a operação selecionada no item 2​
# 7. O sistema deve imprimir na tela caso o acesso foi concedido ou não​
#   1.1 “Acesso permitido” caso o acesso foi concedido​
#   1.2 Se não, “Acesso negado”

#   Importação
import csv

#   Função da interface gráfica
def interface(lista_opcoes, contador=False):
    print('-=' * 15)
    if(not contador):
        for cont, opcao in enumerate(lista_opcoes):
            print(f'[ {cont + 1} ] {opcao}')
    else:
        for opcao in lista_opcoes:
            print(opcao.center(30))
    print('-=' * 15)

#   Função para criar arquivo CSV
def criarAdd_csv(nome_arquivo, dados):
    with open(nome_arquivo, 'a+', newline='') as arquivo:
        writerCSV = csv.writer(arquivo, delimiter=',', lineterminator='\n')
        writerCSV.writerow(dados)

#   Função que para ler arquivo CSV
def ler_csv(nome_arquivo):
    with open(nome_arquivo, 'r', newline='') as arquivo:
        readerCSV = csv.reader(arquivo, delimiter=',')


interface(['Cadastrar', 'Autenticar', 'Sair'])
opcao = input('Opção: ')
if(int(opcao) == 1):
    interface(['CADASTRO'], True)
    username = input('Usuário: ')
    senha = input('Senha')
    criarAdd_csv('usuarios.csv', [])