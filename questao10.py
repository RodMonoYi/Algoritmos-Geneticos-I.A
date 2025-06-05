import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog
from mpl_toolkits.mplot3d import Axes3D

def lucro_surface(x1, x2):
    return 4*x1 + x2

print("--- Parte 1: Otimização de Lucro Original ---")

c = [-4, -1] 
A_ub = [
    [9, 1],
    [3, 1]
]
b_ub = [18, 12] 

x1_bounds = (0, None)
x2_bounds = (0, None)
bounds = [x1_bounds, x2_bounds]

result_original = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

if result_original.success:
    x1_orig, x2_orig = result_original.x
    lucro_orig = lucro_surface(x1_orig, x2_orig) 
    print(f"\n--- Resultado Original ---")
    print(f"Produção ideal (Produto 1): {x1_orig:.2f} unidades")
    print(f"Produção ideal (Produto 2): {x2_orig:.2f} unidades")
    print(f"Lucro máximo (original): ${lucro_orig:.2f}")
else:
    print(f"\nNão foi possível encontrar a solução para a otimização original.")
    print(f"Status: {result_original.message}")

print("\n--- Parte 2: Impacto com Horas-Homem = 15 ---")

b_ub_new = [15, 12] 
result_impacto = linprog(c, A_ub=A_ub, b_ub=b_ub_new, bounds=bounds, method='highs')

if result_impacto.success:
    x1_imp, x2_imp = result_impacto.x
    lucro_imp = lucro_surface(x1_imp, x2_imp)
    print(f"\n--- Resultado com Horas-Homem = 15 ---")
    print(f"Produção ideal (Produto 1): {x1_imp:.2f} unidades")
    print(f"Produção ideal (Produto 2): {x2_imp:.2f} unidades")
    print(f"Lucro máximo (impacto): ${lucro_imp:.2f}")
    print(f"\nImpacto no lucro: ${lucro_orig - lucro_imp:.2f} (redução)")
else:
    print(f"\nNão foi possível encontrar a solução para a otimização com impacto.")
    print(f"Status: {result_impacto.message}")

x1_plot_max = max(x1_orig, x1_imp) + 2 
x2_plot_max = max(x2_orig, x2_imp) + 2 

x1_vals_plot = np.linspace(0, x1_plot_max, 50)
x2_vals_plot = np.linspace(0, x2_plot_max, 50)
X1_mesh, X2_mesh = np.meshgrid(x1_vals_plot, x2_vals_plot)
Z_lucro = lucro_surface(X1_mesh, X2_mesh)

fig = plt.figure(figsize=(14, 10))
ax = fig.add_subplot(111, projection='3d')

surface = ax.plot_surface(X1_mesh, X2_mesh, Z_lucro, cmap='viridis', alpha=0.7)
fig.colorbar(surface, shrink=0.5, aspect=5, label='Lucro')

if result_original.success:
    ax.scatter(x1_orig, x2_orig, lucro_surface(x1_orig, x2_orig), color='red', s=200, marker='o',
               label=f'Ótimo Original (Lucro: ${lucro_orig:.2f})')
if result_impacto.success:
    ax.scatter(x1_imp, x2_imp, lucro_surface(x1_imp, x2_imp), color='blue', s=200, marker='s',
               label=f'Ótimo Impacto (Lucro: ${lucro_imp:.2f})')

x1_line1 = np.linspace(0, x1_plot_max, 100)
x2_line1_orig = 18 - 9*x1_line1
x2_line1_imp = 15 - 9*x1_line1

x2_line2 = 12 - 3*x1_line1

mask_line1_orig = (x2_line1_orig >= 0) & (x2_line1_orig <= x2_plot_max)
mask_line1_imp = (x2_line1_imp >= 0) & (x2_line1_imp <= x2_plot_max)
mask_line2 = (x2_line2 >= 0) & (x2_line2 <= x2_plot_max)


ax.plot(x1_line1[mask_line1_orig], x2_line1_orig[mask_line1_orig], 0, 'k--', linewidth=1, label='$9x_1 + x_2 = 18$ (original)')
ax.plot(x1_line1[mask_line1_imp], x2_line1_imp[mask_line1_imp], 0, 'g--', linewidth=1, label='$9x_1 + x_2 = 15$ (impacto)')
ax.plot(x1_line1[mask_line2], x2_line2[mask_line2], 0, 'purple', linestyle='--', linewidth=1, label='$3x_1 + x_2 = 12$')

ax.plot([0, 0], [0, x2_plot_max], 0, 'k-', linewidth=1, label='$x_1 = 0$')
ax.plot([0, x1_plot_max], [0, 0], 0, 'k-', linewidth=1, label='$x_2 = 0$')

ax.set_xlabel('Produto 1 (x1)')
ax.set_ylabel('Produto 2 (x2)')
ax.set_zlabel('Lucro')
ax.set_title('Maximização do Lucro com Restrições de Produção')
ax.view_init(elev=30, azim=-60)
ax.legend()
plt.tight_layout()


# Para a exibição do gráfico em 3D, você pode usar plt.show() se estiver em um ambiente nativo (com python instalado) ou virtualização com servidor X configurado.
# Caso contrário, salve o gráfico como um arquivo PNG (última linha).

# Para a exibição 3D descomente a linha abaixo e comente a linha de salvar como imagem
# plt.show()

# Caso contrário, para salvar o gráfico como imagem:
plt.savefig('questao10_grafico.png') # Para salvar o gráfico como imagem