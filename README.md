# Análisis de Sistemas M/M/1 con Python

Este repositorio contiene un conjunto de scripts en Python diseñados para analizar y simular sistemas de colas M/M/1. A continuación, se describen las principales secciones del código:

## Dependencias

El código utiliza las siguientes bibliotecas:
- "numpy" para cálculos numéricos y manejo de arreglos.
- "pandas" para la manipulación y análisis de datos.
- "matplotlib" para la generación de visualizaciones.

## Funciones Principales

### "llegada(tiempos_llegada)"
Calcula el parámetro lambda (tasa promedio de llegadas) para un proceso de Poisson. Recibe una lista o arreglo de los tiempos de llegada de los clientes y devuelve el valor de lambda.

### "servicio(tiempos_servicio)"
Calcula el parámetro nu (tasa promedio de servicio) para el proceso de servicio. Toma una lista o arreglo con la duración del servicio a cada cliente y devuelve el valor de nu.

### "parametros(lambda_, nu)"
Determina los parámetros Omega_i, p_i y q_i de un sistema M/M/1 para cada estado, dados lambda y nu.

### "sistema(lambda_, nu, num_clientes)"
Simula un sistema M/M/1 con un número dado de clientes, utilizando los parámetros lambda y nu.

### "visualizacion(tiempos_llegada, tiempos_servicio)"
Crea visualizaciones del sistema M/M/1 a partir de los tiempos de llegada y servicio de los clientes.

### "probabilidad(lambda_, nu, max_estado)"
Calcula el vector de estado estable con la probabilidad de cada estado en un sistema M/M/1.

### "fila(lambda_, nu, L_q, max_estado)"
Calcula el porcentaje del tiempo que la fila del sistema está por encima de un cierto valor L_q.

## Lectura y Análisis de Datos

El código incluye un ejemplo de cómo leer datos de un archivo CSV y aplicar las funciones definidas para analizar un sistema de colas M/M/1.

## Ejemplos de Uso

Se proporcionan ejemplos específicos de cómo utilizar las funciones para simular y analizar un sistema M/M/1, incluyendo la visualización de resultados y el cálculo de probabilidades.
