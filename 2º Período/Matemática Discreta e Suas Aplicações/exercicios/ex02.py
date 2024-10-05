# Importando bibliotecas
import matplotlib.pyplot as plt
import numpy as np

def plot_quadratic(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c

    plt.scatter(x, y, label=f'f(x) = {a}x² + {b}x + {c}')
    plt.plot(x, y)
    plt.title("f(x) = ax² + bx + c")
    plt.xlabel("eixo x")
    plt.ylabel("eixo y")
    plt.legend()
    plt.grid(True, which="both")
    plt.axhline(y=0, color="k")
    plt.axvline(x=0, color="k")
    plt.show()

plot_quadratic(1, -3, 2)

def plot_exponential(a, b):
    x = np.linspace(-10, 10, 400)
    y = a * (b ** x)

    plt.scatter(x, y, label=f'f(x) = {a} * {b}^x')
    plt.plot(x, y)
    plt.title("f(x) = a * b^x")
    plt.xlabel("eixo x")
    plt.ylabel("eixo y")
    plt.legend()
    plt.grid(True, which="both")
    plt.axhline(y=0, color="k")
    plt.axvline(x=0, color="k")
    plt.show()

plot_exponential(2, 1.5)

def plot_modular():
    x = np.linspace(-10, 10, 400)
    y = np.abs(x)

    plt.scatter(x, y, label='f(x) = |x|')
    plt.plot(x, y)
    plt.title("f(x) = |x|")
    plt.xlabel("eixo x")
    plt.ylabel("eixo y")
    plt.legend()
    plt.grid(True, which="both")
    plt.axhline(y=0, color="k")
    plt.axvline(x=0, color="k")
    plt.show()

plot_modular()

def plot_sine():
    x = np.linspace(-10, 10, 400)
    y = np.sin(x)

    plt.scatter(x, y, label='f(x) = sin(x)')
    plt.plot(x, y)
    plt.title("f(x) = sin(x)")
    plt.xlabel("eixo x")
    plt.ylabel("eixo y")
    plt.legend()
    plt.grid(True, which="both")
    plt.axhline(y=0, color="k")
    plt.axvline(x=0, color="k")
    plt.show()

plot_sine()