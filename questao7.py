import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def f(x_array):
    x = x_array[0]
    return x**2 - 3*x + 4
bounds = [(-10, 10)]

x0 = [0.0]

print("--- Otimização para o MÍNIMO (Questão 7) ---")
result_min = minimize(f, x0, method='L-BFGS-B', bounds=bounds, options={'disp': True})

if result_min.success:
    x_min_found = result_min.x[0]
    f_min_found = result_min.fun
    print(f"\nO valor de x que MINIMIZA a função é: {x_min_found:.6f}")
    print(f"O valor MÍNIMO da função f(x) é: {f_min_found:.6f}")
else:
    print(f"\nNão foi possível encontrar o MÍNIMO da função.")
    print(f"Status da otimização: {result_min.message}")

x_vals = np.linspace(-10, 10, 400)
f_vals = f([x_vals])

plt.figure(figsize=(10, 6))
plt.plot(x_vals, f_vals, label='$f(x) = x^2 - 3x + 4$')
plt.scatter(x_min_found, f_min_found, color='red', s=100, marker='o',
            label=f'Mínimo Encontrado ($x={x_min_found:.2f}$, $f(x)={f_min_found:.2f}$)')

plt.title('Minimização da Função $f(x) = x^2 - 3x + 4$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

# Para a exibição do gráfico em 3D, você pode usar plt.show() se estiver em um ambiente nativo (com python instalado) ou virtualização com servidor X configurado.
# Caso contrário, salve o gráfico como um arquivo PNG (última linha).

# Para a exibição 3D descomente a linha abaixo e comente a linha de salvar como imagem
# plt.show()

# Caso contrário, para salvar o gráfico como imagem:
plt.savefig('questao7_grafico.png') # Para salvar o gráfico como imagem