# Exercício: Preencha a matriz 50x seguindo o seguinte pseudo código, e meça o tempo:
'''
Início
Criar uma matriz chamada buffer com 4096 linhas e 4096 colunas
Para cada linha i de 0 até 4095 faça
    Para cada coluna j de 0 até 4095 faça
        buffer[i][j] ← (i + j) módulo 256
Fim
'''
import time 

buffer = [[0] * 4096 for _ in range(4096)]

def preencher_buffer():
    for i in range(4096):
        for j in range(4096):
            buffer[i][j] = (i + j) % 256

tempo_inicial = time.perf_counter()
for _ in range(50):  # Executa apenas uma vez para medir o tempo
    preencher_buffer()
tempo_final = time.perf_counter()

tempo_execucao = tempo_final - tempo_inicial
print(f"Tempo de execução 1: {tempo_execucao} segundos")


# Exercício: Preencha a matriz x50, só que agora, faça o preenchimento em colunas e depois das linhas (inverta i com j).
buffer = [[0] * 4096 for _ in range(4096)]

tempo_inicial = time.perf_counter()
for _ in range(50):  # Executa apenas uma vez para medir o tempo
    preencher_buffer()
tempo_final = time.perf_counter()

tempo_execucao = tempo_final - tempo_inicial
print(f"Tempo de execução 2: {tempo_execucao} segundos")

# Compare o resultado e explique o porque da diferença.
# R: O tempo de execução pode ser diferente devido ao acesso à memória cache. No primeiro caso, o acesso é feito em linhas, o que pode aproveitar melhor a localidade espacial da cache. No segundo caso, o acesso é feito em colunas, o que pode resultar em mais faltas de cache e, portanto, um tempo de execução maior.