import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

c = [-100, -80, -120, -30] 

A_ub = [
    [1, 1, 1, 4],   # Tábuas
    [0, 1, 1, 2],   # Pranchas
    [3, 2, 4, 0]    # Painéis
]
b_ub = [300, 600, 500] 

x_bounds = (0, None)
bounds = [x_bounds, x_bounds, x_bounds, x_bounds]

print("--- Otimização de Lucro da Fábrica de Móveis (Questão 11) ---")

result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

if result.success:
    x1_opt, x2_opt, x3_opt, x4_opt = result.x
    
    max_lucro = -result.fun
    
    print(f"\n--- Resultado da Produção Ótima ---")
    print(f"Quantidades a fabricar para maximizar o lucro:")
    print(f"  Escrivaninhas (x1): {x1_opt:.2f} unidades")
    print(f"  Mesas (x2):         {x2_opt:.2f} unidades")
    print(f"  Armários (x3):      {x3_opt:.2f} unidades")
    print(f"  Prateleiras (x4):   {x4_opt:.2f} unidades")
    print(f"\nLucro máximo total: ${max_lucro:.2f}")

    recursos_utilizados = np.dot(A_ub, result.x)
    print("\n--- Recursos Utilizados vs. Disponíveis ---")
    print(f"  Tábuas:       {recursos_utilizados[0]:.2f}m / {b_ub[0]}m")
    print(f"  Pranchas:     {recursos_utilizados[1]:.2f}m / {b_ub[1]}m")
    print(f"  Painéis:      {recursos_utilizados[2]:.2f}m / {b_ub[2]}m")

else:
    print(f"\nNão foi possível encontrar a solução ótima.")
    print(f"Status da otimização: {result.message}")


# Para um problema de PL com 4 variáveis, uma visualização 3D completa é impossível
# A melhor representação de "mesh" em PL é um gráfico 2D da região viável
# se considerarmos 2 variáveis principais e fixarmos as outras ou projetarmos
# No entanto, com 4 variáveis, um plot 2D das restrições de cada par de variáveis não é suficiente
# O mais direto é mostrar o resultado numericamente
# Pra um plot, a gente pode fixar x3=0 e x4=0 para visualizar as restrições em x1 e x2

print("\n--- Visualização da Região Viável (x3=0, x4=0 para ilustração 2D) ---")
x1_plot_vals = np.linspace(0, 200, 400)
x2_plot_vals = np.linspace(0, 300, 400)

plt.figure(figsize=(10, 8))
plt.plot(x1_plot_vals, 300 - x1_plot_vals, label='Tábuas ($x_1 + x_2 \\leq 300$)')
plt.axhline(y=600, color='grey', linestyle='--', label='Pranchas ($x_2 \\leq 600$)')
plt.plot(x1_plot_vals, (500 - 3*x1_plot_vals) / 2, label='Painéis ($3x_1 + 2x_2 \\leq 500$)')

plt.axvline(x=0, color='k', linestyle='-')
plt.axhline(y=0, color='k', linestyle='-')

if result.success:
    if abs(x3_opt) < 1e-6 and abs(x4_opt) < 1e-6: 
        plt.scatter(x1_opt, x2_opt, color='red', s=100, marker='o',
                    label=f'Ótimo Geral: $x_1$={x1_opt:.0f}, $x_2$={x2_opt:.0f}')
    else:
        print("\nNota: O ponto ótimo real não está neste plano 2D (x3=0, x4=0).")


plt.xlim(-5, 200)
plt.ylim(-5, 300)
plt.xlabel('Quantidade de Escrivaninhas ($x_1$)')
plt.ylabel('Quantidade de Mesas ($x_2$)')
plt.title('Região Viável das Restrições (x3=0, x4=0)')
plt.legend()
plt.grid(True)

# Para a exibição do gráfico em 3D, você pode usar plt.show() se estiver em um ambiente nativo (com python instalado) ou virtualização com servidor X configurado.
# Caso contrário, salve o gráfico como um arquivo PNG (última linha).

# Para a exibição 3D descomente a linha abaixo e comente a linha de salvar como imagem
# plt.show()

# Caso contrário, para salvar o gráfico como imagem:
plt.savefig('questao11_regiao_viável.png') # Para salvar o gráfico como imagem