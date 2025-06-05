import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from mpl_toolkits.mplot3d import Axes3D

def lucro_function(xy_array):
    x, y = xy_array
    return 60*x + 100*y - (3/2)*x**2 - (3/2)*y**2 - x*y
def neg_lucro_function(xy_array):
    return -lucro_function(xy_array)

bounds = [(0, None), (0, None)]

x0 = [10.0, 10.0] 

print("--- Otimização para MAXIMIZAR o Lucro (Questão 8) ---")
result_max_lucro = minimize(neg_lucro_function, x0, method='L-BFGS-B', bounds=bounds, options={'disp': True})
if result_max_lucro.success:
    x_opt, y_opt = result_max_lucro.x
    max_lucro = -result_max_lucro.fun 
    print(f"\n--- Resultados da Otimização de Lucro ---")
    print(f"Produção que maximiza o lucro:")
    print(f"  Produto A (x): {x_opt:.2f} unidades")
    print(f"  Produto B (y): {y_opt:.2f} unidades")
    print(f"Lucro máximo esperado: {max_lucro:.2f}")
else:
    print(f"\nNão foi possível encontrar a produção que maximiza o lucro.")
    print(f"Status da otimização: {result_max_lucro.message}")

x_vals_plot = np.linspace(0, 50, 100)
y_vals_plot = np.linspace(0, 50, 100)
X, Y = np.meshgrid(x_vals_plot, y_vals_plot)

Z = lucro_function([X, Y])

fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')
surface = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, rstride=5, cstride=5)
fig.colorbar(surface, shrink=0.5, aspect=5, label='Lucro L(x, y)')

if result_max_lucro.success:
    ax.scatter(x_opt, y_opt, max_lucro, color='red', s=200, marker='o',
               label=f'Lucro Máximo: (x={x_opt:.0f}, y={y_opt:.0f}, L={max_lucro:.0f})')

ax.set_xlabel('Unidades do Produto A (x)')
ax.set_ylabel('Unidades do Produto B (y)')
ax.set_zlabel('Lucro L(x, y)')
ax.set_title('Superfície de Lucro da Indústria')

ax.view_init(elev=30, azim=45) 
ax.legend()
plt.tight_layout()


# Para a exibição do gráfico em 3D, você pode usar plt.show() se estiver em um ambiente nativo (com python instalado) ou virtualização com servidor X configurado.
# Caso contrário, salve o gráfico como um arquivo PNG (última linha).

# Para a exibição 3D descomente a linha abaixo e comente a linha de salvar como imagem
# plt.show()

# Caso contrário, para salvar o gráfico como imagem:
plt.savefig('questao8_grafico.png') # Para salvar o gráfico como imagem