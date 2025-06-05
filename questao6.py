import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from mpl_toolkits.mplot3d import Axes3D 

def f(x_array):
    x1, x2 = x_array
    return (x1**2 + x2**2 - 1)**2

def neg_f(x_array):
    return -f(x_array)

def constraint1(x): 
    return x[0] + x[1] - 1

def constraint2(x): 
    return x[0] * x[1] - 0.5

def constraint3(x): 
    return x[1] - x[0]**2

def constraint4(x):
    return x[0] - x[1]**2

constraints = [
    {'type': 'ineq', 'fun': constraint1},
    {'type': 'ineq', 'fun': constraint2},
    {'type': 'ineq', 'fun': constraint3},
    {'type': 'ineq', 'fun': constraint4}
]

bounds = [(-1, 1), (-1, 1)]
x0 = [1.0, 1.0]

print("--- Otimização para o MÍNIMO ---")
result_min = minimize(f, x0, method='SLSQP', bounds=bounds, constraints=constraints, options={'disp': True})

print("\n--- Otimização para o MÁXIMO ---")
result_max = minimize(neg_f, x0, method='SLSQP', bounds=bounds, constraints=constraints, options={'disp': True})

print("\n--- Resultados da Otimização (Questão 6) ---")

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

x1_vals_plot = np.linspace(bounds[0][0], bounds[0][1], 100)
x2_vals_plot = np.linspace(bounds[1][0], bounds[1][1], 100)
X1, X2 = np.meshgrid(x1_vals_plot, x2_vals_plot)
Z = f([X1, X2])

fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

surface = ax.plot_surface(X1, X2, Z, cmap='coolwarm', alpha=0.8)
fig.colorbar(surface, shrink=0.5, aspect=5, label='f(x1, x2)')

ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$f(x_1, x_2)$')
ax.set_title('Superfície da Função $f(x_1, x_2)$ com Restrições (Questão 6)')

if result_min.success:
    ax.scatter(x_min[0], x_min[1], f_min, color='green', s=150, marker='o', label=f'Mínimo Ot. ({x_min[0]:.2f}, {x_min[1]:.2f}, {f_min:.2f})')
if result_max.success:
    ax.scatter(x_max[0], x_max[1], f_max, color='red', s=150, marker='s', label=f'Máximo Ot. ({x_max[0]:.2f}, {x_max[1]:.2f}, {f_max:.2f})')

ax.plot(x1_vals_plot, 1 - x1_vals_plot, np.zeros_like(x1_vals_plot), 'k--', linewidth=1, label='$x_1+x_2=1$')

x1_curve = np.linspace(0.1, 1.0, 100)
x2_curve = 0.5 / x1_curve
mask_curve = (x1_curve >= bounds[0][0]) & (x1_curve <= bounds[0][1]) & \
             (x2_curve >= bounds[1][0]) & (x2_curve <= bounds[1][1])
ax.plot(x1_curve[mask_curve], x2_curve[mask_curve], np.zeros_like(x1_curve[mask_curve]), 'm--', linewidth=1, label='$x_1x_2=0.5$')

ax.plot(x1_vals_plot, x1_vals_plot**2, np.zeros_like(x1_vals_plot), 'c--', linewidth=1, label='$x_2=x_1^2$')

ax.plot(x2_vals_plot**2, x2_vals_plot, np.zeros_like(x2_vals_plot), 'y--', linewidth=1, label='$x_1=x_2^2$')

ax.view_init(elev=30, azim=45)
ax.legend()
plt.tight_layout()

# Para a exibição do gráfico em 3D, você pode usar plt.show() se estiver em um ambiente nativo (com python instalado) ou virtualização com servidor X configurado.
# Caso contrário, salve o gráfico como um arquivo PNG (última linha).

# Para a exibição 3D descomente a linha abaixo e comente a linha de salvar como imagem
# plt.show()

# Caso contrário, para salvar o gráfico como imagem:
plt.savefig('questao6_grafico.png') 