import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from mpl_toolkits.mplot3d import Axes3D 

def f(x_array):
    x1, x2 = x_array
    return 0.5 * x1**2 + x2**2 - x1*x2 - 2*x1 - 6*x2

def neg_f(x_array):
    return -f(x_array)

constraints = [
    {'type': 'ineq', 'fun': lambda x: 2 - x[0] - x[1]},
    {'type': 'ineq', 'fun': lambda x: 2 + x[0] - x[1]},
    {'type': 'ineq', 'fun': lambda x: 3 - 2*x[0] - 2*x[1]}
]

bounds = [(0, None), (0, None)]

x0 = [0.5, 0.5]

# 4. Otimização para Mínimo
print("--- Otimização para o MÍNIMO ---")
result_min = minimize(f, x0, method='SLSQP', bounds=bounds, constraints=constraints)
x_min = result_min.x
f_min = result_min.fun
print(f"O valor de x1 e x2 que MINIMIZA a função é: x1={x_min[0]:.4f}, x2={x_min[1]:.4f}")
print(f"O valor MÍNIMO da função f(x) é: {f_min:.4f}\n")

print("--- Otimização para o MÁXIMO ---")
result_max = minimize(neg_f, x0, method='SLSQP', bounds=bounds, constraints=constraints)
x_max = result_max.x
f_max = -result_max.fun 
print(f"O valor de x1 e x2 que MAXIMIZA a função é: x1={x_max[0]:.4f}, x2={x_max[1]:.4f}")
print(f"O valor MÁXIMO da função f(x) é: {f_max:.4f}\n")

x1_vals = np.linspace(-0.5, 2.5, 100)
x2_vals = np.linspace(-0.5, 2.5, 100)
X1, X2 = np.meshgrid(x1_vals, x2_vals)
Z = f([X1, X2]) 

fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

surface = ax.plot_surface(X1, X2, Z, cmap='viridis', alpha=0.7, rstride=5, cstride=5)
fig.colorbar(surface, shrink=0.5, aspect=5, label='f(x1, x2)')

ax.scatter(x_min[0], x_min[1], f_min, color='red', s=150, marker='o', label=f'Mínimo: ({x_min[0]:.2f}, {x_min[1]:.2f}, {f_min:.2f})')
ax.scatter(x_max[0], x_max[1], f_max, color='blue', s=150, marker='s', label=f'Máximo: ({x_max[0]:.2f}, {x_max[1]:.2f}, {f_max:.2f})')

ax.plot(x1_vals, 2 - x1_vals, 0, color='gray', linestyle='--', label='$x_1 + x_2 = 2$')
ax.plot(x1_vals, 2 + x1_vals, 0, color='gray', linestyle='--', label='$-x_1 + x_2 = 2$')
ax.plot(x1_vals, (3 - 2*x1_vals) / 2, 0, color='gray', linestyle='--', label='$2x_1 + 2x_2 = 3$')

ax.plot([0, 0], [x2_vals.min(), x2_vals.max()], 0, color='gray', linestyle='--', label='$x_1 = 0$')
ax.plot([x1_vals.min(), x1_vals.max()], [0, 0], 0, color='gray', linestyle='--', label='$x_2 = 0$')

ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$f(x_1, x_2)$')
ax.set_title('Otimização da Função $f(x_1, x_2)$ com Restrições')
ax.view_init(elev=30, azim=-45) # Ajustar o ângulo de visão
ax.legend()
plt.tight_layout()

# Para a exibição do gráfico em 3D, você pode usar plt.show() se estiver em um ambiente nativo (com python instalado) ou virtualização com servidor X configurado.
# Caso contrário, salve o gráfico como um arquivo PNG (última linha).

# Para a exibição 3D descomente a linha abaixo e comente a linha de salvar como imagem
# plt.show()

# Caso contrário, para salvar o gráfico como imagem:
plt.savefig('questao3_grafico.png') 