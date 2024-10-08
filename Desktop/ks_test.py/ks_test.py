# Importar las bibliotecas necesarias
import numpy as np
from scipy import stats

# Generar 100 números aleatorios entre 0 y 1
random_numbers = np.random.uniform(0, 1, 100)

# Aplicar la prueba de Kolmogorov-Smirnov para la uniformidad
ks_statistic, p_value = stats.kstest(random_numbers, 'uniform')

# Mostrar los resultados
print(f"Estadístico de Kolmogorov-Smirnov: {ks_statistic:.5f}")
print(f"Valor p: {p_value:.5f}")

# Evaluar si los datos son uniformes
if p_value > 0.05:
    print("No se puede rechazar la hipótesis nula: los números parecen tener una distribución uniforme.")
else:
    print("Se rechaza la hipótesis nula: los números no tienen una distribución uniforme.")
