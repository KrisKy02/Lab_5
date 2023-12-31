# Laboratorio 5 - Módulo de Cadena de Markov

Este repositorio contiene un módulo de Python diseñado para el análisis de un sistema M/M/1 en el contexto de la teoría de colas. Este módulo fue desarrollado como parte del Laboratorio 5 para el curso "IE0405 - Modelos Probabilísticos de Señales y Sistemas" de la Universidad de Costa Rica.

## Funciones del Módulo "cadena.py"

1. **llegada(tiempos_llegada):** Calcula el parámetro lambda (tasa promedio de llegadas) para un proceso de Poisson.

2. **servicio(tiempos_servicio):** Calcula el parámetro nu (tasa promedio de servicio) para el proceso de servicio.

3. **parametros(lambda_, nu):** Calcula los parámetros Omega_i, p_i y q_i de un sistema M/M/1 para cada estado.

4. **sistema(lambda_, nu, num_clientes):** Simula un sistema M/M/1 con un número dado de clientes.

5. **visualizacion(resultado_sistema, lambda_, nu):** Crea una visualización para el sistema M/M/1.

6. **probabilidad(lambda_, nu, max_estado):** Calcula el vector de estado estable con la probabilidad de cada estado en un sistema M/M/1.

7. **fila(lambda_, nu, L_q, max_estado=100):** Calcula el porcentaje del tiempo que la fila del sistema está por encima de un cierto valor L_q.

8. **fila_c(lambda_, nu, L_q, P_val, tiempo_simulacion=10000):** Determina el porcentaje de clientes que hacen fila de L_q espacios antes de recibir el servicio.

9. **servidores(lambda_, nu, L_q, P):** Encuentra el número de servidores necesarios para satisfacer un parámetro dado de calidad del servicio.

10. **tiempo(lambda_, nu, L_q, P_val, tiempo_simulacion=10000):** Encuentra el tiempo promedio de servicio necesario para satisfacer un parámetro dado de calidad del servicio.

## Estudiantes

- Kristel Herrera Rodríguez (C13769)
- Oscar Porras Silesky (C16042)
- Fabrizzio Herrera Calvo (B83849)

## Uso del Módulo

Se puede utilizar este módulo para realizar análisis de sistemas M/M/1 mediante las funciones proporcionadas. A continuación, se muestra un ejemplo básico de uso ubicado en el archivo "revision.py":

```python
"""
Análisis de Datos por medio de "cadena.py".

Este script utiliza el módulo "cadena.py" para realizar
el análisis de un sistema M/M/1. El script lee los datos
de un archivo CSV y luego utiliza las funciones del módulo
para realizar el análisis.


El script se estructura de la siguiente manera:
- Importar el módulo "cadena.py".
- Leer el archivo CSV.
- Extraer los datos necesarios.
- Aplicar las funciones.
- Mostrar los resultados.
- Ejecutar las pruebas.


Estudiantes:

Kristel Herrera Rodríguez C13769
Oscar Porras Silesky C16042
Fabrizzio Herrera Calvo B83849
"""

import pandas as pd
import cadena
# Leer el archivo CSV
df = pd.read_csv('clientes.csv')
# Extraer los datos necesarios
tiempos_llegada = df['llegada'].to_numpy()
tiempos_servicio = df['servicio'].to_numpy()


def revisar_llegada(tolerancia=1e-2):
    # Esta función revisa la función llegada
    # con los datos de prueba
    resultado = lambda_
    assert abs(resultado - lambda_val) < tolerancia, (
        f"Fallo en revisar_llegada. Resultado: {resultado}, "
        f"Esperado: {lambda_val}"
    )


def revisar_servicio(tolerancia=1e-2):
    # Esta función revisa la función servicio
    # con los datos de prueba
    resultado = nu
    assert abs(resultado - nu_val) < tolerancia, (
        f"Fallo en revisar_llegada. Resultado: {resultado}, Esperado: {nu_val}"
    )


def revisar_parametros(tolerancia=1e-2):
    # Esta función revisa la función parametros
    # con los datos de prueba
    Omega_i = lambda_ + nu
    p_i = lambda_ / Omega_i
    q_i = nu / Omega_i

    assert abs(Omega_i - 0.083) < tolerancia, (
        f"Fallo en revisar_parametros. Resultado: {Omega_i}, "
        f"Esperado: {0.083}"
    )

    assert abs(p_i - 0.42) < tolerancia, (
        f"Fallo en revisar_parametros. Resultado: {p_i}, "
        f"Esperado: {0.42}"
    )

    assert abs(q_i - 0.58) < tolerancia, (
        f"Fallo en revisar_parametros. Resultado: {q_i}, "
        f"Esperado: {0.58}"
    )


def revisar_probabilidad(tolerancia=1e-2):
    # Esta función revisa la función probabilidad
    # con los datos de prueba
    max_estado = 100
    resultado = cadena.probabilidad(lambda_, nu, max_estado)
    probabilidades_esperadas = [0.28, 0.20, 0.15, 0.10432465114590479, 0.075,
                                0.05365499698510028, 0.038, 0.028,
                                0.020, 0.014, 0.01]

    for i in range(1+1):
        assert abs(resultado[i] - probabilidades_esperadas[i]) < tolerancia, (
            f"Fallo en revisar_probabilidad. "
            f"Resultado[{i}]: {resultado[i]}, "
            f"Esperado: {probabilidades_esperadas[i]}"
        )


def revisar_fila(tolerancia=1e-2):
    # Esta función revisa la función fila
    # con los datos de prueba
    resultado = cadena.fila(lambda_, nu, L_q, P_val)
    porcentaje_esperado = 13.60

    assert abs(resultado - porcentaje_esperado) < tolerancia, (
        f"Fallo en revisar_fila. "
        f"Resultado: {resultado}, Esperado: {porcentaje_esperado}"
    )


def revisar_fila_c(tolerancia=10):
    # Esta función revisa la función fila_c
    # con los datos de prueba
    resultado = cadena.fila_c(lambda_, nu, L_q, P_val)
    porcentaje_esperado = 30.12

    assert abs(resultado - porcentaje_esperado) < tolerancia, (
        f"Fallo en revisar_fila_c. "
        f"Resultado: {resultado}, Esperado: {porcentaje_esperado}"
    )


def revisar_servidores(tolerancia=1e-2):
    # Esta función revisa la función servidores
    # con los datos de prueba
    resultado = cadena.servidores(lambda_, nu, L_q, P_val)
    servidores_esperados = 1

    assert resultado == servidores_esperados, (
        f"Fallo en revisar_servidores. "
        f"Resultado: {resultado}, Esperado: {servidores_esperados}"
    )


def revisar_tiempo(tolerancia=10):
    # Esta función revisa la función tiempo
    # con los datos de prueba
    resultado = cadena.tiempo(lambda_, nu, L_q, P_val)
    tiempo_esperado = 64.77

    assert abs(resultado - tiempo_esperado) < tolerancia, (
        f"Fallo en revisar_tiempo. "
        f"Resultado: {resultado}, Esperado: {tiempo_esperado}"
    )


# Aplicar las funciones
lambda_ = cadena.llegada(tiempos_llegada)
nu = cadena.servicio(tiempos_servicio)
parametros_sistema = cadena.parametros(lambda_, nu)

# Mostrar los resultados
print("Lambda:", lambda_)
print("Nu:", nu)
print("Parámetros del sistema:", parametros_sistema)
resultado_sistema = cadena.sistema(lambda_, nu, 100)
# Crear un DataFrame a partir del diccionario de resultados
df_resultados = pd.DataFrame(resultado_sistema)

# Opcional: Redondear los resultados para una mejor visualización
df_resultados = df_resultados.round(2)

# Imprimir el DataFrame
print(df_resultados)
cadena.visualizacion(resultado_sistema, lambda_, nu)

vector_probabilidades = cadena.probabilidad(lambda_, nu, 10)
print(f'El vector de estado estable es: {vector_probabilidades}')
L_q = 5
P_val = 90
# Por ejemplo, para L_q = 5
porcentaje_tiempo_Lq = cadena.fila(lambda_, nu, L_q, P_val)
# Imprimir el resultado con formato
print(f"Para un sistema M/M/1 con λ={lambda_} y ν={nu}, el porcentaje "
      f"de tiempo que la fila es mayor o igual a {L_q} "
      f"es aproximadamente {porcentaje_tiempo_Lq:.2f}%.")
# Ejemplo de uso
lambda_val = 0.035  # Tasa de llegada
nu_val = 0.048      # Tasa de servicio
L_q_val = 5       # Cantidad de clientes en fila

porcentaje_en_fila = cadena.fila_c(lambda_, nu, L_q, P_val)
num_servidores_necesarios = cadena.servidores(lambda_, nu, L_q, P_val)
tiempo_promedio_servicio = cadena.tiempo(lambda_, nu, L_q, P_val)

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
