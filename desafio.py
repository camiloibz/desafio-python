import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pathlib


nombre_archivos = ["data_plantas_python_1_1.xlsx", "data_plantas_python_2.xlsx"]
nombre_hoja_excel = ['planta1', 'Sheet1']

for i in range(len(nombre_archivos)):
    df = pd.read_excel(nombre_archivos[i], sheet_name=nombre_hoja_excel[i])
    data_a_usar = df[['fecha_im', 'active_energy_im', 'active_power_im']] #selección de las columnas que poseen los datos requeridos
    data_a_usar = data_a_usar.dropna() #elimina filas con valores nulos
    data_faltante = data_a_usar['active_power_im'] != 'data_faltante' #filtro de filas con data faltante
    data_a_usar = data_a_usar[data_faltante] #elimina las filas que no entran en el filtro anterior

    fechas = data_a_usar['fecha_im'].tolist()
    active_power = data_a_usar['active_power_im'].tolist()

    suma_active_power = data_a_usar['active_power_im'].sum()
    min_active_energy = data_a_usar['active_energy_im'].min()
    max_active_energy = data_a_usar['active_energy_im'].max()

    #GRÁFICO DE LÍNEAS
    x = np.array(fechas)
    y = np.array(active_power)
    plt.plot(x, y)
    plt.title("Generación de energía de la planta " + str(i + 1))
    plt.xlabel("Fecha")
    plt.ylabel("Active power")
    plt.savefig("grafico_planta_" + str(i + 1) + ".png")
    plt.clf()

    #OUTPUT ARCHIVO DE TEXTO
    f = open("txt_planta_" + str(i + 1) + ".txt", "w")
    f.write("Suma total del active power de la planta " + str(i + 1) + ": " + str(suma_active_power) + "\n")
    f.write("Valor minimo del active energy de la planta " + str(i + 1) + ": " + str(min_active_energy) + "\n")
    f.write("Valor maximo del active energy de la planta " + str(i + 1) + ": " + str(max_active_energy) + "\n")
    f.write("Ruta del grafico generado: " + str(pathlib.Path(__file__).parent.absolute()) + "/grafico_planta_" + str(i + 1) + ".png")

    #OUTPUT CONSOLA
    print("Suma total del active power de la planta " + str(i + 1) + ": " + str(suma_active_power))
