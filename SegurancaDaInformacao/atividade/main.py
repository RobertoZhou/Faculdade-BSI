# 1. Criar ambiente virtual do Python (O comando do python pode ser diferente na sua máquina)
#    python3 -m venv venv

# 2. Ativar ambiente virtual
#    Linux: source venv/bin/activate
#    Windows (CMD): venv\Scripts\Activate.bat

# 3. Instalar dependências
#    pip install pyrebase4 setuptools

# 4. Configurar Firebase

import pyrebase

# firebaseConfig = (insira a API)

#   Autenticar no FireBase
APP = pyrebase.initialize_app(firebaseConfig)

# Criar API para acessar a aplicação de autenticação
AUTH = APP.auth()

# # Criar usuário
# email = "womija9348@provko.com"
# senha = "pucpr@1234"
# #token = AUTH.create_user_with_email_and_password(email, senha)

# # Autenticar Usuário
# token = AUTH.sign_in_with_email_and_password(email, senha)

# # Mostra informação do token do usuário
# print(token)

# # Mostra informações do usuário
# id_token = token['idToken']
# print(AUTH.get_account_info(id_token))

# 1. Criar dois usuários
#   1.1 Solicitar credenciais pelo terminal (input)
#   1.2 Verificar se o e-mail já existe
#   1.3 Criar conta caso e-mail não exista
# 2. Mostrar as informações do token do usuário
# 3. Enviar e-mail de confirmação de e-mail

while True:
    email = input("Digite seu Email: ")
    senha = input("Crie uma senha: ")
    try:
        token = AUTH.create_user_with_email_and_password(email, senha)
        token_user = AUTH.sign_in_with_email_and_password(email, senha)
        break
    except:
        print("ERRO! USUÁRIO JÁ CADASTRADO!")
        continue
    
print(token)
AUTH.send_email_verification(token_user['idToken'])
print('E-mail enviado!')