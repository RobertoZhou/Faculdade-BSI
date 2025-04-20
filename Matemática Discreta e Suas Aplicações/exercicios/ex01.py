# Importando bibliotecas
import matplotlib.pyplot as plt
import numpy as np

# Função do primeiro grau
def funcao1oGrau(a, b, x):
    return (a * x + b)

vetorX = np.arange(-5, 5, 1)
print(vetorX)

a = 2
b = 5
vetorY = funcao1oGrau(a, b, vetorX)  # Calcula os valores de y

# Criando uma janela (figura)
fig = plt.figure(figsize=(10, 10))
# Plotando ponto a ponto do vetor x com o respectivo y
plt.plot(vetorX, vetorY, label="Função 1° Grau")
# Função para mostrar a janela
plt.legend()  # Adiciona legenda
plt.show()