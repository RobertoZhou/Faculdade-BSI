# Faça um programa Python que calcule uma aproximação para PI com 100 Milhões de termos
import time
start_time = time.time()
'''
def calcular_pi(num_termos):
    pi = 0
    for k in range(num_termos):
        pi += ((-1) ** k) / (2 * k + 1)
    return pi * 4

aproximacao_pi = calcular_pi(100_000_000)
print(aproximacao_pi)

end_time = time.time()
print("Tempo de execução:", end_time - start_time)
'''

# Melhorando a performance com Numpy
import numpy as np
def calcular_pi_numpy(num_termos):
    k = np.arange(num_termos)
    pi = np.sum((-1) ** k / (2 * k + 1))
    return pi * 4
aproximacao_pi_numpy = calcular_pi_numpy(100_000_000)
print(aproximacao_pi_numpy)
end_time = time.time()
print("Tempo de execução com Numpy:", end_time - start_time)
