import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def objective(x):
    x1, x2 = x
    return 100 * (x1**2 - x2)**2 + (1 - x1)**2

def constraint1(x):
    x1, x2 = x
    return -(x1 * x2 + x1 - x2 + 1.5) 

def constraint2(x):
    x1, x2 = x
    return -(10 - x1 - x2) 

constraints = [
    {'type': 'ineq', 'fun': constraint1},
    {'type': 'ineq', 'fun': constraint2}
]

bounds = [(0, 1), (0, 3)]

x0 = [0.5, 0.5]

result = minimize(objective, x0, bounds=bounds, constraints=constraints)

x1_vals = np.linspace(0, 1, 100)
x2_vals = np.linspace(0, 3, 100)
X1, X2 = np.meshgrid(x1_vals, x2_vals)
Z = 100 * (X1**2 - X2)**2 + (1 - X1)**2

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X1, X2, Z, cmap='viridis', alpha=0.8, edgecolor='k')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('f(x)')

x_opt, y_opt = result.x
z_opt = objective(result.x)
ax.scatter(x_opt, y_opt, z_opt, color='red', s=50, label='Mínimo encontrado')
ax.legend()

plt.title('Otimização com Restrições - Questão 5')

# Para a exibição do gráfico em 3D, você pode usar plt.show() se estiver em um ambiente nativo (com python instalado) ou virtualização com servidor X configurado.
# Caso contrário, salve o gráfico como um arquivo PNG (última linha).

# Para a exibição 3D descomente a linha abaixo e comente a linha de salvar como imagem
# plt.show()

# Caso contrário, para salvar o gráfico como imagem:
plt.savefig("questao5_grafico.png")
