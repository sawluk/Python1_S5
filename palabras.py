import numpy as np

# Generar un array de 365 elementos representando los precios diarios de la acción
precios_diarios = np.random.uniform(50, 150, 365)

# Calcular el rendimiento diario como la diferencia porcentual entre los precios consecutivos
rendimiento_diario = np.diff(precios_diarios) / precios_diarios[:-1] * 100

# Calcular el rendimiento medio y la desviación estándar del rendimiento diario
rendimiento_medio = np.mean(rendimiento_diario)
desviacion_estandar = np.std(rendimiento_diario)

# Calcular el rendimiento acumulado durante todo el año
rendimiento_acumulado_anual = (precios_diarios[-1] - precios_diarios[0]) / precios_diarios[0] * 100

# Imprimir los resultados
print("Rendimiento diario (primeros 10 elementos):")
print(rendimiento_diario[:10])
print("\nRendimiento medio:", rendimiento_medio)
print("Desviación estándar del rendimiento:", desviacion_estandar)
print("Rendimiento acumulado durante todo el año:", rendimiento_acumulado_anual)




