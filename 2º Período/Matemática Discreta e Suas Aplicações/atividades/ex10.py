# Faça um menu que só encerre quando o usuário solicitar (opção de sair) que seja interativo e com as
# devidas validações de possíveis erros de entrada do usuário. O objetivo é fazer a operação entre 2 conjuntos,
# ou seja, crie uma forma de pedir dois conjuntos para o usuário (conjuntos A e B – posteriormente esses
# conjuntos podem ser alterados pelo usuário). As opções de operações são:
#   1) União
#   2) Intersecção
#   3) Diferença
#   4) Produto cartesiano
#   5) Verificação se A é subconjunto de B (submenu: subconjunto ou subconjunto próprio)
#   6) Mesma verificação do item e, mas de B com A.

#   Função menu
def menu(listaOpcao):
    for cont, opcao in enumerate(listaOpcao):
        print(f"{cont+1} - {opcao.capitalize()}")
    while True:
        print("=" * 25)
        escolha = input("Opção[Somente Números]: ")
        if(escolha.isnumeric()):
            if(int(escolha) <= len(listaOpcao) and int(escolha) > 0):
                return int(escolha)
        print("Opção Inválida!")
        continue

#   Função adicionar elementos ao conjunto
def addConjunto(nomeConjunto, varConjunto):
    print(f"Conjunto {nomeConjunto}:")
    while True:
        elemento = input("Adicionando elemento: ")
        if(elemento.isnumeric()):
            elemento = int(elemento)
        varConjunto.add(elemento)
        opcoes = ["continuar adicionando", "finalizar conjunto"]
        opcao = menu(opcoes)
        if(opcao == 2):
            return varConjunto
        
def resolucaoConjunto(nomeConjunto1, conjunto1, nomeConjunto2, conjunto2, opcao):
    if(opcao == 1):
        print(f"{nomeConjunto1} ∪ {nomeConjunto2} = {conjunto1.union(conjunto2)}")
    elif(opcao == 2):
        print(f"{nomeConjunto1} ∩ {nomeConjunto2} = {conjunto1.intersection(conjunto2)}")
    elif(opcao == 3):
        print(f"{nomeConjunto1} - {nomeConjunto2} = {conjunto1.difference(conjunto2)}")
    elif(opcao == 4):
        produto_cartesiano = {(a, b) for a in conjunto1 for b in conjunto2}
        print(f"{nomeConjunto1} X {nomeConjunto2} = {produto_cartesiano}")
    elif(opcao == 5):
        if(conjunto1.issubset(conjunto2) and conjunto1 != conjunto2):
            print(f"{nomeConjunto1} ⊂ {nomeConjunto2}")
        else:
            print(f"{nomeConjunto1} ⊆ {nomeConjunto2}")
    else:
        print("Opção Inválida!")

conjuntoA = set()
conjuntoB = set()

listaOpcoes = ["adicionar conjunto", "sair"]
opcao = menu(listaOpcoes)
if(opcao != 2):
    while opcao != 7:
        A = addConjunto("A", conjuntoA)
        print(f"A = {A}")
        B = addConjunto("B", conjuntoB)
        print(f"B = {B}")
        print("=" * 25)
        while True:
            listaOpcoes = ["A com B", "B com A"]
            formatacao = menu(listaOpcoes)

            listaOpcoes = ["mostrar união", "mostrar intersecção", "mostrar diferença", "mostrar produto cartesiano", "verificar subconjunto/subconjunto próprio", "resetar conjuntos", "sair"]
            opcao = menu(listaOpcoes)
            if(opcao == 7):
                break

            print("=" * 25)
            if(formatacao == 1):
                resolucaoConjunto("A", A, "B", B, opcao)
            elif(formatacao == 2):
                resolucaoConjunto("B", B, "A", A, opcao)
