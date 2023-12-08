# revision.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import lab5
# Leer el archivo CSV
df = pd.read_csv('clientes.csv')
# Extraer los datos necesarios
tiempos_llegada = df['llegada'].to_numpy()
tiempos_servicio = df['servicio'].to_numpy()

def revisar_llegada(tolerancia=1e-2):
    resultado = lambda_
    assert abs(resultado - lambda_val) < tolerancia , f"Fallo en revisar_llegada. Resultado: {resultado}, Esperado: {lambda_val}"

def revisar_servicio(tolerancia=1e-2):
    resultado = nu
    assert abs(resultado - nu_val) < tolerancia , f"Fallo en revisar_llegada. Resultado: {resultado}, Esperado: {nu_val}"

def revisar_parametros(tolerancia=1e-2):
    Omega_i = lambda_ + nu
    p_i = lambda_ / Omega_i
    q_i = nu / Omega_i
    assert abs(Omega_i - 0.083) < tolerancia , f"Fallo en revisar_llegada. Resultado: {Omega_i}, Esperado: {0.083}"
    assert abs(p_i - 0.42) < tolerancia , f"Fallo en revisar_llegada. Resultado: {p_i}, Esperado: {0.42}"
    assert abs(q_i - 0.58) < tolerancia , f"Fallo en revisar_llegada. Resultado: {q_i}, Esperado: {0.58}"

def revisar_probabilidad(tolerancia=1e-2):
    max_estado = 100
    resultado = lab5.probabilidad(lambda_, nu,max_estado)
    probabilidades_esperadas = [0.28, 0.20, 0.15, 0.10432465114590479, 0.075, 0.05365499698510028, 0.038, 0.028, 0.020, 0.014, 0.01]
    
    for i in range(1+1):
        assert abs(resultado[i] - probabilidades_esperadas[i]) < tolerancia, \
            f"Fallo en revisar_probabilidad. Resultado[{i}]: {resultado[i]}, Esperado: {probabilidades_esperadas[i]}"

def revisar_fila(tolerancia=1e-2):
    resultado = lab5.fila(lambda_, nu, L_q, P_val)
    porcentaje_esperado = 13.60
    
    assert abs(resultado - porcentaje_esperado) < tolerancia, f"Fallo en revisar_fila. Resultado: {resultado}, Esperado: {porcentaje_esperado}"
    
def revisar_fila_c(tolerancia=10):
    resultado = lab5.fila_c(lambda_, nu, L_q, P_val)
    porcentaje_esperado = 30.12
    
    assert abs(resultado - porcentaje_esperado) < tolerancia, \
        f"Fallo en revisar_fila_c. Resultado: {resultado}, Esperado: {porcentaje_esperado}"
    
def revisar_servidores(tolerancia=1e-2):
    resultado = lab5.servidores(lambda_, nu, L_q, P_val)
    servidores_esperados = 1
    
    assert resultado == servidores_esperados, \
        f"Fallo en revisar_servidores. Resultado: {resultado}, Esperado: {servidores_esperados}"

def revisar_tiempo(tolerancia=10):
    resultado = lab5.tiempo(lambda_, nu, L_q, P_val)
    tiempo_esperado = 64.77
    
    assert abs(resultado - tiempo_esperado) < tolerancia, \
        f"Fallo en revisar_tiempo. Resultado: {resultado}, Esperado: {tiempo_esperado}"
# Agregar cualquier observación adicional o comentarios necesarios
# Leer el archivo CSV
df = pd.read_csv('clientes.csv')


# Aplicar las funciones
lambda_ = lab5.llegada(tiempos_llegada)
nu = lab5.servicio(tiempos_servicio)
parametros_sistema = lab5.parametros(lambda_, nu)

# Mostrar los resultados
print("Lambda:", lambda_)
print("Nu:", nu)
print("Parámetros del sistema:", parametros_sistema)
resultado_sistema = lab5.sistema(lambda_, nu, 100)
# Crear un DataFrame a partir del diccionario de resultados
df_resultados = pd.DataFrame(resultado_sistema)

# Opcional: Redondear los resultados para una mejor visualización
df_resultados = df_resultados.round(2)

# Imprimir el DataFrame
print(df_resultados)
lab5.visualizacion(resultado_sistema,lambda_,nu)

vector_probabilidades = lab5.probabilidad(lambda_, nu, 10)
print(f'El vector de estado estable es: {vector_probabilidades}')
L_q = 5
P_val = 90
porcentaje_tiempo_Lq = lab5.fila(lambda_, nu, L_q, P_val)  # Por ejemplo, para L_q = 5
# Imprimir el resultado con formato
print(f"Para un sistema M/M/1 con λ={lambda_} y ν={nu}, el porcentaje de tiempo que la fila es mayor o igual a {L_q} es aproximadamente {porcentaje_tiempo_Lq:.2f}%.")
# Ejemplo de uso
lambda_val = 0.035  # Tasa de llegada
nu_val = 0.048      # Tasa de servicio
L_q_val = 5       # Cantidad de clientes en fila

porcentaje_en_fila = lab5.fila_c(lambda_, nu, L_q, P_val)
num_servidores_necesarios = lab5.servidores(lambda_, nu, L_q, P_val)
tiempo_promedio_servicio = lab5.tiempo(lambda_, nu, L_q, P_val)

print(f"Porcentaje de clientes en fila: {porcentaje_en_fila}%")
print(f"Número de servidores necesarios: {num_servidores_necesarios}")
print(f"Tiempo promedio de servicio necesario: {tiempo_promedio_servicio}")

# Ejecutar las pruebas
revisar_llegada(tolerancia=1e-2)
revisar_servicio(tolerancia=1e-2)
revisar_parametros(tolerancia=1e-2)
revisar_probabilidad(tolerancia=1e-2)
revisar_fila(tolerancia=1e-2)
revisar_fila_c(tolerancia=10)
revisar_servidores(tolerancia=1e-2)
revisar_tiempo(tolerancia=10)
print("Todas las pruebas pasaron exitosamente.")
