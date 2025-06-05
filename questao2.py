import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x1, x2):
    return (x1**2 + x2**2 - 1)**2

x1_min, x1_max = -1, 1
x2_min, x2_max = -1, 1

num_points = 50
x1_vals = np.linspace(x1_min, x1_max, num_points)
x2_vals = np.linspace(x2_min, x2_max, num_points)
X1, X2 = np.meshgrid(x1_vals, x2_vals)

Z = f(X1, X2)

min_f_val = 0.0

max_points = [
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
]
max_f_val = f(max_points[0][0], max_points[0][1])

print(f"--- Resultados da Análise (Questão 2) ---")
print(f"Valor Mínimo da função: {min_f_val:.4f}")
print(f"Ocorre em qualquer ponto (x1, x2) onde x1^2 + x2^2 = 1, dentro da região definida.")
print(f"Valor Máximo da função: {max_f_val:.4f}")
print(f"Ocorre nos pontos: {max_points}")

fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

surface = ax.plot_surface(X1, X2, Z, cmap='viridis', alpha=0.8, rstride=1, cstride=1)

fig.colorbar(surface, shrink=0.5, aspect=5, label='f(x1, x2) - Valor da Função')

for p in max_points:
    ax.scatter(p[0], p[1], f(p[0], p[1]), color='red', s=100, marker='o', label='Máximo Encontrado' if p == max_points[0] else "")

theta = np.linspace(0, 2*np.pi, 100)
circle_x1 = np.cos(theta)
circle_x2 = np.sin(theta)
mask = (circle_x1 >= x1_min) & (circle_x1 <= x1_max) & \
       (circle_x2 >= x2_min) & (circle_x2 <= x2_max)
ax.plot(circle_x1[mask], circle_x2[mask], np.zeros_like(circle_x1[mask]), 'b--', linewidth=2, label='Localização dos Mínimos (Z=0)')


ax.set_xlabel('$x_1$')
ax.set_ylabel('$x_2$')
ax.set_zlabel('$f(x_1, x_2)$')
ax.set_title('Superfície da Função $f(x_1, x_2) = (x_1^2 + x_2^2 - 1)^2$')

ax.view_init(elev=30, azim=45) 

plt.legend()
plt.tight_layout() # Ajusta o layout para evitar sobreposição


# Para a exibição do gráfico em 3D, você pode usar plt.show() se estiver em um ambiente nativo (com python instalado) ou virtualização com servidor X configurado.
# Caso contrário, salve o gráfico como um arquivo PNG (última linha).

# Para a exibição 3D descomente a linha abaixo e comente a linha de salvar como imagem
# plt.show()

# Caso contrário, para salvar o gráfico como imagem:
plt.savefig('questao2_grafico.png')

