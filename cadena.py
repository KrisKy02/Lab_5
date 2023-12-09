"""
Laboratorio 5.

IE0405 - Modelos Probabilísticos de Señales y Sistemas
Universidad de Costa Rica

Módulo de Cadena de Markov para el Laboratorio 5.

Este módulo contiene un conjunto de funciones diseñadas para realizar el
análisis de un sistema M/M/1.

Funciones:
- llegada: Calcula el parámetro lambda (tasa promedio de llegadas)
           para un proceso de Poisson.
- servicio: Calcula el parámetro nu (tasa promedio de servicio)
            para el proceso de servicio.
- parametros: Calcula los parámetros Omega_i, p_i y q_i
              de un sistema M/M/1 para cada estado.
- sistema: Simula un sistema M/M/1 con un número dado de clientes.
- visualizacion: Crea una visualización para el sistema M/M/1.
- probabilidad: Calcula el vector de estado estable con la
                probabilidad de cada estado en un sistema M/M/1.
- fila: Calcula el porcentaje del tiempo que la fila del
        sistema está por encima de un cierto valor L_q.
- fila_c: Determina el porcentaje de clientes que hacen fila de L_q
          espacios antes de recibir el servicio.
- servidores: Encuentra el número de servidores necesarios
              para satisfacer un parámetro dado de calidad del servicio.
- tiempo: Encuentra el tiempo promedio de servicio necesario
          para satisfacer un parámetro dado de calidad del servicio.


Estudiantes:

Kristel Herrera Rodríguez C13769
Oscar Porras Silesky C16042
Fabrizzio Herrera Calvo B83849

"""


import numpy as np
import matplotlib.pyplot as plt
import math


def llegada(tiempos_llegada):
    """
    Calcula el parámetro lambda (tasa promedio de llegadas)
    para un proceso de Poisson.

    :param tiempos_llegada: Lista o arreglo de los
                            tiempos de llegada de los clientes.
    :return: Valor del parámetro lambda.
    """
    # Calcular los intervalos entre llegadas
    intervalos = np.diff(tiempos_llegada)

    # Calcular la tasa promedio de llegadas (lambda)
    lambda_ = 1 / np.mean(intervalos)

    return lambda_


def servicio(tiempos_servicio):
    """
    Calcula el parámetro nu (tasa promedio de servicio)
    para el proceso de servicio.

    :param tiempos_servicio: Lista o arreglo con la
                             duración del servicio a cada cliente.
    :return: Valor del parámetro nu.
    """
    # Calcular la tasa promedio de servicio (nu)
    nu = 1 / np.mean(tiempos_servicio)

    return nu


def parametros(lambda_, nu):
    """
    Calcula los parámetros Omega_i, p_i y q_i
    de un sistema M/M/1 para cada estado.

    :param lambda_: Tasa promedio de llegadas (lambda).
    :param nu: Tasa promedio de servicio (nu).
    :return: Diccionario con los valores de Omega_i, p_i y q_i.
    """
    # Calcular Omega_i, p_i y q_i
    Omega_i = lambda_ + nu
    p_i = lambda_ / Omega_i
    q_i = nu / Omega_i

    return {"Omega_i": Omega_i, "p_i": p_i, "q_i": q_i}


def sistema(lambda_, nu, num_clientes):
    """
    Simula un sistema M/M/1 con un número dado de clientes.

    :param lambda_: Tasa promedio de llegadas.
    :param nu: Tasa promedio de servicio.
    :param num_clientes: Número de clientes a simular.
    :return: Diccionario con tiempos de llegada,
             inicio de servicio, fin de servicio,
             tiempo en el sistema y tiempo en la cola para cada cliente.
    """
    # Inicializar listas para almacenar los tiempos
    tiempos_llegada = np.cumsum(np.random.exponential(1/lambda_, num_clientes))
    inicio_servicio = np.zeros(num_clientes)
    fin_servicio = np.zeros(num_clientes)

    # El primer cliente es atendido inmediatamente al llegar
    inicio_servicio[0] = tiempos_llegada[0]
    fin_servicio[0] = inicio_servicio[0] + np.random.exponential(1/nu)

    # Calcular los tiempos para los siguientes clientes
    for i in range(1, num_clientes):
        inicio_servicio[i] = max(tiempos_llegada[i], fin_servicio[i - 1])
        fin_servicio[i] = inicio_servicio[i] + np.random.exponential(1/nu)

    # Calcular el tiempo en el sistema y en la cola para cada cliente
    tiempo_en_sistema = fin_servicio - tiempos_llegada
    tiempo_en_cola = inicio_servicio - tiempos_llegada

    return {
        "tiempos_llegada": tiempos_llegada,
        "inicio_servicio": inicio_servicio,
        "fin_servicio": fin_servicio,
        "tiempo_en_sistema": tiempo_en_sistema,
        "tiempo_en_cola": tiempo_en_cola
    }


def visualizacion(resultado_sistema, lambda_, nu):
    """
    Crea una visualización para el sistema M/M/1.

    :param resultado_sistema: Diccionario con tiempos
                              de llegada, inicio de servicio, fin de servicio,
                              tiempo en el sistema y tiempo en la cola.
    """
    tiempos_llegada = resultado_sistema['tiempos_llegada']
    fin_servicio = resultado_sistema['fin_servicio']

    # Crear una secuencia de tiempos para la visualización
    tiempos = np.sort(np.concatenate((tiempos_llegada, fin_servicio)))
    clientes_en_sistema = np.array([np.sum((tiempos_llegada <= t)
                                           & (fin_servicio > t))
                                    for t in tiempos])

    # Crear el gráfico
    plt.figure(figsize=(12, 6))
    plt.step(tiempos, clientes_en_sistema, where='post')
    plt.xlabel('Tiempo')
    plt.ylabel('Número de Clientes en el Sistema')
    plt.title(f'Clientes en el Sistema M/M/1 a'
              f'lo Largo del Tiempo (λ={lambda_}, ν={nu})')
    plt.grid(True)
    plt.show()


def probabilidad(lambda_, nu, max_estado):
    """
    Calcula el vector de estado estable con la
    probabilidad de cada estado en un sistema M/M/1.

    :param lambda_: Tasa promedio de llegadas (lambda).
    :param nu: Tasa promedio de servicio (nu).
    :param max_estado: Número máximo de estado
                       para calcular las probabilidades.
    :return: Vector con las probabilidades de estado estable.
    """
    rho = lambda_ / nu
    probabilidades = [(1 - rho) * rho**n for n in range(max_estado + 1)]

    return probabilidades


def fila(lambda_, nu, L_q, max_estado=100):
    """
    Calcula el porcentaje del tiempo que la fila del
    sistema está por encima de un cierto valor L_q.

    :param lambda_: Tasa promedio de llegadas (lambda).
    :param nu: Tasa promedio de servicio (nu).
    :param L_q: Tamaño de la fila que se considera como límite.
    :param max_estado: Número máximo de estado para
                       los cálculos (opcional, por defecto 100).
    :return: Porcentaje del tiempo que la fila es mayor o igual a L_q.
    """
    probabilidades = probabilidad(lambda_, nu, max_estado)
    probabilidad_fila_Lq = sum(probabilidades[L_q + 1:])

    return probabilidad_fila_Lq * 100


def fila_c(lambda_, nu, L_q, P_val, tiempo_simulacion=10000):
    """
    Determina el porcentaje de clientes que hacen fila de L_q
    espacios antes de recibir el servicio.

    :param lambda_: Tasa promedio de llegadas (lambda).
    :param nu: Tasa promedio de servicio (nu).
    :param L_q: Cantidad de clientes en fila.
    :param P: Porcentaje de tiempo deseado.
    :param tiempo_simulacion: Número de iteraciones para la simulación.
    :return: Porcentaje de clientes en fila.
    """
    resultados_sistema = sistema(lambda_, nu, tiempo_simulacion)
    tiempo_en_cola = resultados_sistema["tiempo_en_cola"]

    a = tiempo_en_cola
    b = tiempo_simulacion
    fraccion_tiempo_cumple_condicion = np.sum(a > 0) / b
    porcentaje_cumple_condicion = (1 - fraccion_tiempo_cumple_condicion) * 100

    return porcentaje_cumple_condicion


def servidores(lambda_, nu, L_q, P):
    """
    Encuentra el número de servidores necesarios
    para satisfacer un parámetro dado de calidad del servicio.

    :param lambda_: Tasa promedio de llegadas (lambda).
    :param nu: Tasa promedio de servicio (nu).
    :param L_q: Cantidad de clientes en fila.
    :param P: Porcentaje de tiempo deseado.
    :return: Número de servidores necesarios.
    """
    s = math.ceil(L_q / (100 - P))
    return s


def tiempo(lambda_, nu, L_q, P_val, tiempo_simulacion=10000):
    """
    Encuentra el tiempo promedio de servicio necesario
    para satisfacer un parámetro dado de calidad del servicio.

    :param lambda_: Tasa promedio de llegadas (lambda).
    :param nu: Tasa promedio de servicio (nu).
    :param L_q: Cantidad de clientes en fila.
    :param P: Porcentaje de tiempo deseado.
    :param tiempo_simulacion: Número de iteraciones para la simulación.
    :return: Tiempo promedio de servicio necesario.
    """
    resultados_sistema = sistema(lambda_, nu, tiempo_simulacion)
    tiempo_promedio_servicio = np.mean(resultados_sistema["tiempo_en_sistema"])

    return tiempo_promedio_servicio
