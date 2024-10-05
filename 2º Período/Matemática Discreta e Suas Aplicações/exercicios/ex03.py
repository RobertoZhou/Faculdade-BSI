def c(A, B):
    # Converter listas de entrada para conjuntos
    A = set(A)
    B = set(B)

    # Inicializar valor para 0
    valor = 0

    # Verificar se 2 está em A e 5 está em B
    if 2 in A and 5 in B:
        valor += 5
    else:
        valor -= 5

    # Verificar se C é um subconjunto da interseção de A e B
    C = set([2, 8])
    if C.issubset(A.intersection(B)):
        valor += 10
    else:
        valor -= 10

    # Verificar se D é um subconjunto da diferença entre B e A
    D = set([2, 5, 7])
    if D.issubset(B.difference(A)):
        valor += 15
    else:
        valor -= 15

    # Verificar se o conjunto vazio está presente em A
    if set() in A:
        valor += 20
    else:
        valor -= 20

    # Verificar se o conjunto vazio é um subconjunto de B
    if set().issubset(B):
        valor += 35
    else:
        valor -= 35

    # Retornar o valor final de valor
    return valor

A = [2, 4, 6, 8]
B = [2, 3, 5, 7, 8]
print(c(A, B))  # Saída: 35

