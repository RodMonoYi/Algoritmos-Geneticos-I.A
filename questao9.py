import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from mpl_toolkits.mplot3d import Axes3D

def area_function(xy_array):
    x, y = xy_array
    return x*y + 8/y + 8/x

epsilon = 1e-6
bounds = [(epsilon, None), (epsilon, None)]

x0 = [2.0, 2.0]

print("--- Otimização para MINIMIZAR a Área da Superfície (Questão 9) ---")

result_min_area = minimize(area_function, x0, method='L-BFGS-B', bounds=bounds, options={'disp': True})

if result_min_area.success:
    x_opt, y_opt = result_min_area.x

    volume_fixo = 4
    z_opt = volume_fixo / (x_opt * y_opt)

    min_area = result_min_area.fun
    
    print(f"\n--- Resultados da Otimização da Caixa ---")
    print(f"Dimensões que minimizam a área:")
    print(f"  x (comprimento): {x_opt:.4f} m")
    print(f"  y (largura):     {y_opt:.4f} m")
    print(f"  z (altura):      {z_opt:.4f} m")
    print(f"Área mínima da superfície: {min_area:.4f} m²")
    print(f"Volume verificado: {x_opt * y_opt * z_opt:.4f} m³ (deve ser aproximadamente 4)")
else:
    print(f"\nNão foi possível encontrar as dimensões que minimizam a área.")
    print(f"Status da otimização: {result_min_area.message}")

x_vals_plot = np.linspace(0.5, 4.0, 50)
y_vals_plot = np.linspace(0.5, 4.0, 50)
X_plot, Y_plot = np.meshgrid(x_vals_plot, y_vals_plot)

Z_area = np.zeros_like(X_plot)
for i in range(X_plot.shape[0]):
    for j in range(X_plot.shape[1]):
        current_x = X_plot[i, j]
        current_y = Y_plot[i, j]
        if current_x > epsilon and current_y > epsilon:
            Z_area[i, j] = area_function([current_x, current_y])
        else:
            Z_area[i, j] = np.inf

fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

surface = ax.plot_surface(X_plot, Y_plot, Z_area, cmap='jet', alpha=0.8, rstride=1, cstride=1)
fig.colorbar(surface, shrink=0.5, aspect=5, label='Área da Superfície A(x, y) m²')

if result_min_area.success:
    ax.scatter(x_opt, y_opt, min_area, color='red', s=200, marker='o',
               label=f'Área Mínima: ({x_opt:.2f}, {y_opt:.2f}, {min_area:.2f})')

ax.set_xlabel('Comprimento (x) m')
ax.set_ylabel('Largura (y) m')
ax.set_zlabel('Área da Superfície (A) m²')
ax.set_title('Área da Superfície da Caixa Retangular sem Tampa')

ax.view_init(elev=30, azim=45)
ax.legend()
plt.tight_layout()


# Para a exibição do gráfico em 3D, você pode usar plt.show() se estiver em um ambiente nativo (com python instalado) ou virtualização com servidor X configurado.
# Caso contrário, salve o gráfico como um arquivo PNG (última linha).

# Para a exibição 3D descomente a linha abaixo e comente a linha de salvar como imagem
# plt.show()

# Caso contrário, para salvar o gráfico como imagem:
plt.savefig('questao9_grafico.png') # Para salvar o gráfico como imagem