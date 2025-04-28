import pandas as pd
import matplotlib.pyplot as plt

# %%
df = pd.read_csv("casos_coronavirus.csv")
df.head()

df.info()

#%% Convertimos la columna de casos nuevos a np.array
casos_diarios = df.confirmados_Nuevos.values

#%% Graficamos la serie de casos diarios
plt.plot(casos_diarios)

# %% Calculamos la cantidad de casos acumulados con la funcion cumsum
cum_casos = casos_diarios.cumsum()
plt.plot(cum_casos)
plt.show()

# %% Tomamos logaritmos para linealizar (convertimos los datos primero a float
#    para poder tomar logaritmo)
plt.plot(np.log(np.float64(cum_casos)))

#%% Alternativamente, podemos mantener los datos "al natural" y cambiar la
#   _escala_ del eje y
plt.plot(cum_casos), plt.yscale("log")
plt.show()