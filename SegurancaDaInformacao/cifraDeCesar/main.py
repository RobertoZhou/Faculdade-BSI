'''
Implementar Cifra de Cesar
    -Python ou Java
    -Cifrar a mensagem
        "If you want to keep a secret, you must also hide it from yourself."
    -Considerar k = 1, k = 3 e k = 23
'''

def cifra_de_cesar(mensagem, k):
    resultado = ""
    
    # Itera sobre cada caractere da mensagem
    for i in range(len(mensagem.upper())):
        char = mensagem[i]
        
        # Verifica se o caractere é uma letra maiúscula
        if char.isalpha():
            resultado += chr((ord(char) + k - 65) % 26 + 65)
        else:
            resultado += char
    
    return resultado
    
print(cifra_de_cesar("If you want to keep a secret, you must also hide it from yourself.", 1))
print(cifra_de_cesar("If you want to keep a secret, you must also hide it from yourself.", 3))
print(cifra_de_cesar("If you want to keep a secret, you must also hide it from yourself.", 23))