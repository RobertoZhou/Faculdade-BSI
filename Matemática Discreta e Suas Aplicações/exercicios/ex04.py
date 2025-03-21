def ver(A, B):
    # Converter listas de entrada para conjuntos
    A = set(A)
    B = set(B)

    # Verificar se B é um subconjunto próprio de A
    if B.issubset(A) and A != B:
        print("verdadeiro")
        return True
    print("Falso")
    return False

A = set([1, 2, 3])
B = set([3, 2])
C = set([1, 4, 3])
D = C.difference(B)
E = set([4, 5, 6, 7])
F = C.difference(E)
F = F.union(B)
print(F)  # Imprime o conjunto resultante F
ver(A, F)  # Verifica se F é um subconjunto próprio de A
