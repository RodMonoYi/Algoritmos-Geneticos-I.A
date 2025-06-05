import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from mpl_toolkits.mplot3d import Axes3D # Corrigido para Axes3D

def f(x_array):
    x1, x2 = x_array
    return 100 * (x2 - x1**2)**2 + (1 - x1)**2

def neg_f(x_array):
    return -f(x_array)

def non_linear_constraint(x_array):
    x1, x2 = x_array
    return -((x1 - 1/3)**2 + (x2 - 1/3)**2 + (1/3)**2)

constraints = [
    {'type': 'ineq', 'fun': non_linear_constraint}
]

bounds = [(0, 0.5), (0.2, 0.8)]

x0 = [0.25, 0.5]

print("--- Otimização para o MÍNIMO ---")
result_min = minimize(f, x0, method='SLSQP', bounds=bounds, constraints=constraints, options={'disp': True})

print("\n--- Otimização para o MÁXIMO ---")
result_max = minimize(neg_f, x0, method='SLSQP', bounds=bounds, constraints=constraints, options={'disp': True})

print("\n--- Resultados da Otimização (Questão 4) ---")

if result_min.success:
    x_min = result_min.x
    f_min = result_min.fun
    print(f"Mínimo Encontrado:")
    print(f"  x1={x_min[0]:.6f}, x2={x_min[1]:.6f}")
    print(f"  Valor Mínimo de f(x) = {f_min:.6f}")
else:
    print(f"Não foi possível encontrar o MÍNIMO da função.")
    print(f"Status da otimização para o mínimo: {result_min.message}")

if result_max.success:
    x_max = result_max.x
    f_max = -result_max.fun
    print(f"\nMáximo Encontrado:")
    print(f"  x1={x_max[0]:.6f}, x2={x_max[1]:.6f}")
    print(f"  Valor Máximo de f(x) = {f_max:.6f}")
else:
    print(f"\nNão foi possível encontrar o MÁXIMO da função.")
    print(f"Status da otimização para o máximo: {result_max.message}")

# NOTE: Como a região viável é vazia, o plot de pontos ótimos será omitido ou estará fora do domínio.
# O gráfico ainda pode mostrar a superfície da função dentro dos limites dados.

# Geração da malha para o gráfico 3D dentro dos limites
x1_vals_plot = np.linspace(bounds[0][0], bounds[0][1], 50)
x2_vals_plot = np.linspace(bounds[1][0], bounds[1][1], 50)
X1, X2 = np.meshgrid(x1_vals_plot, x2_vals_plot)
Z = f([X1, X2])

fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

surface = ax.plot_surface(X1, X2, Z, cmap='plasma', alpha=0.8)
fig.colorbar(surface, shrink=0.5, aspect=5, label='f(x1, x2)')

ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$f(x_1, x_2)$')
ax.set_title('Superfície da Função de Rosenbrock (Questão 4)')

if result_min.success:
    ax.scatter(x_min[0], x_min[1], f_min, color='red', s=150, marker='o', label=f'Mínimo Ot. ({x_min[0]:.2f}, {x_min[1]:.2f}, {f_min:.2f})')
if result_max.success:
    ax.scatter(x_max[0], x_max[1], f_max, color='blue', s=150, marker='s', label=f'Máximo Ot. ({x_max[0]:.2f}, {x_max[1]:.2f}, {f_max:.2f})')

ax.view_init(elev=30, azim=45)
ax.legend()
plt.tight_layout()


# Para a exibição do gráfico em 3D, você pode usar plt.show() se estiver em um ambiente nativo (com python instalado) ou virtualização com servidor X configurado.
# Caso contrário, salve o gráfico como um arquivo PNG (última linha).

# Para a exibição 3D descomente a linha abaixo e comente a linha de salvar como imagem
# plt.show()

# Caso contrário, para salvar o gráfico como imagem:
plt.savefig('questao4_grafico.png') 