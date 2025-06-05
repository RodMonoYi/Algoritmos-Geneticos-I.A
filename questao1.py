import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution

def objective_function(x_array):
    x = x_array[0]

    g_x = (2**(-2 * ((x - 0.1) / 0.9)**2)) * (np.sin(5 * np.pi * x)**6)

    return -g_x

bounds = [(0, 1)] # xmin = 0, xmax = 1

result = differential_evolution(objective_function, bounds, disp=True, strategy='best1bin', maxiter=1000, popsize=15)

x_otimo = result.x[0] 
min_neg_g_x = result.fun 

max_g_x = -min_neg_g_x

print(f"\n--- Resultados da Otimização (Questão 1) ---")
print(f"O valor de x que maximiza a função é: {x_otimo:.6f}")
print(f"O valor máximo da função g(x) é: {max_g_x:.6f}")

x_vals = np.linspace(0, 1, 1000)
g_vals = (2**(-2 * ((x_vals - 0.1) / 0.9)**2)) * (np.sin(5 * np.pi * x_vals)**6)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, g_vals, label='$g(x) = 2^{-2((x-0.1)/0.9)^2} \sin(5\pi x)^6$')
plt.plot(x_otimo, max_g_x, 'ro', markersize=8, label=f'Máximo Encontrado ($x={x_otimo:.4f}$, $g(x)={max_g_x:.4f}$)')

plt.title('Maximização da Função g(x) usando Differential Evolution')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid(True)
plt.legend()
plt.ylim(bottom=0) 

# Para a exibição do gráfico em 3D, você pode usar plt.show() se estiver em um ambiente nativo (com python instalado) ou virtualização com servidor X configurado.
# Caso contrário, salve o gráfico como um arquivo PNG (última linha).

# Para a exibição 3D descomente a linha abaixo e comente a linha de salvar como imagem
# plt.show()

# Caso contrário, para salvar o gráfico como imagem:
plt.savefig('questao1_grafico.png')